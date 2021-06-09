# Scanner of ports
Scanner of ports - web-приложениедля сканирования открытых 
TCP портов удаленного хоста.

## Реализует слудующее REST API
GET /scan/<ip>/<begin_port>/<end_port>
* ip - хост, который необходимо просканировать
* begin_port - начало диапазона портов для сканирования
* end_port - конец диапазона
   

## Используемые технологии
* Python 3.8;
* aiohttp

## До запуска приложения
1. Создайте виртуальное окружение
2. Установите зависимости pip install -r requirements.txt
3. Запустите scanner_of_ports.py