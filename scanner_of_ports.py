from aiohttp import web
import asyncio
import logging

from scanner_services import scanning_range_of_ports


logging.basicConfig(filename="sample.log", level=logging.INFO)

async def handler(request):
    logging.info('Processing started')
    answer = []
    # Проверка корректности данных, вводимых пользователем
    ip = request.match_info['ip'].strip()
    ip_list = ip.split('.')
    ip_list_str = [number for number in ip.split('.') if number.isdigit()]
    ip_list_int = [int(number) for number in ip_list_str if 0 <= int(number) <= 255]
    
    if len(ip_list_int) == 4:
        try:            
            begin_port = int(request.match_info['begin_port'].strip())
            end_port = int(request.match_info['end_port'].strip())
        except ValueError:
            logging.info(
                f"ValueError: begin_port {request.match_info['begin_port']}, end_port {request.match_info['end_port']}")
            return web.Response(text='Неверно введен(ы) порт(ы)')
        # Запуск сканирования портов
        await scanning_range_of_ports(ip, begin_port, end_port, answer)
        logging.info('Scan finished')
        return web.json_response(answer)
    
    logging.info(f'Invalid ip address {ip}')
    return web.Response(text='Неверно введен ip-адрес')


app = web.Application()
app.add_routes([web.get('/scan/{ip}/{begin_port}/{end_port}', handler)])
web.run_app(app)
