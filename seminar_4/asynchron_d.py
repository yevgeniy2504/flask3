# Задание
#
# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. Каждое изображение
# должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе. Например,
# URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg — Программа должна использовать
# многопоточный, многопроцессорный и асинхронный подходы. — Программа должна иметь возможность задавать список
# URL-адресов через аргументы командной строки. — Программа должна выводить в консоль информацию о времени скачивания
# каждого изображения и общем времени выполнения программы.


import asyncio
import os
from pathlib import Path
import aiohttp
import time
import requests
from synchronize_method import data_image
import argparse

initial_time = time.time()

parser = argparse.ArgumentParser(description="Парсер изображений")
parser.add_argument("--urls", default=data_image, nargs="+", help="список URL адресов для загрузке изображений")
args = parser.parse_args()


urls = args.urls
if not urls:
    urls = data_image




async def download(img):
    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        response = requests.get(img, stream=True)
        filename = Path('./img/').joinpath("asinc_" + os.path.basename(img))
        with open(filename, 'wb') as f:
            for chank in response.iter_content(chunk_size=1024):
                if chank:
                    f.write(chank)
        end_time = time.time() - start_time
        print(f"Загрузка {filename} завершена за {end_time:.2f} секунд")


async def main():
    tasks = []
    for img in urls:
        task = asyncio.ensure_future(download(img))
        tasks.append(task)
    await asyncio.gather(*tasks)


start_time = time.time()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(f"всего затрачено времени {time.time() - initial_time:.2f}")
