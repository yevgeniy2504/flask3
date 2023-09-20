import argparse
from pathlib import Path
import requests
import os
import time

data_image = ['https://mirpozitiva.ru/wp-content/uploads/2019/11/1472042805_21-768x480.jpg',
              'https://mirpozitiva.ru/wp-content/uploads/2019/11/1472042492_01-768x480.jpg',
              'https://mirpozitiva.ru/wp-content/uploads/2019/11/1472042485_04-768x432.jpg',
              'https://mirpozitiva.ru/wp-content/uploads/2019/11/1472043884_02.jpg',
              'https://mirpozitiva.ru/wp-content/uploads/2019/11/1472042585_06-768x480.jpg',
              ]

parser = argparse.ArgumentParser(description="Парсер изображений")
parser.add_argument("--urls", default=data_image, nargs="+", help="список URL адресов для загрузке изображений")
args = parser.parse_args()
urls = args.urls
if not urls:
    urls = data_image


def synchronize_download(img_pefix, img):
    start_time = time.time()
    response = requests.get(img, stream=True)
    filename = Path('./img/').joinpath(img_pefix + os.path.basename(img))
    with open(filename, 'wb') as f:
        for chank in response.iter_content(chunk_size=1024):
            if chank:
                f.write(chank)
    end_time = time.time() - start_time
    print(f"Загрузка {filename} завершена за {end_time:.2f} секунд")


img_pefix = 'multiprocessing_'


if __name__ == '__main__':
    for img in urls:
        synchronize_download(img_pefix, img)








