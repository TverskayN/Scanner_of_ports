import asyncio

async def tcp_echo_client(ip, port, answer):
    # Проверяет открыт ли порт
    try:
        reader, writer = await asyncio.open_connection(
            ip, port, limit=0.1)
        answer.append({"port": port, "state": "open"})
    except TimeoutError:
        answer.append({"port": port, "state": "close"})

async def tasks_scanning_range_of_ports(ip, begin_port, end_port, answer):
    # Создает task для сканирования портов (включая границы).
    # Печатает ответ в формате [{"port": port, "state": "(open|close)"}]
    tasks = []
    for port in range(begin_port, end_port+1):
        tasks.append(asyncio.create_task(tcp_echo_client(ip, port, answer)))
    for task in tasks:
        await task

async def scanning_range_of_ports(ip, begin_port, end_port, answer):
    # Запускает tasks для сканирования диапазона портов
    await tasks_scanning_range_of_ports(ip, begin_port, end_port, answer)
