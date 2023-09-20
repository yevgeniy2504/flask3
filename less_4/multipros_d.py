import argparse

import requests
from multiprocessing import Process
import time
from synchronize_method import data_image, synchronize_download

parser = argparse.ArgumentParser(description="Парсер изображений")
parser.add_argument("--urls", default=data_image, nargs="+", help="список URL адресов для загрузке изображений")
args = parser.parse_args()
urls = args.urls
if not urls:
    urls = data_image


processes = []
start_time = time.time()

if __name__ == '__main__':
    for img in urls:
        process = Process(target=synchronize_download, args=("multiprocess_", img,))
        processes.append(process)
        process.start()
        for process in processes:
            process.join()
        print(f"всего затрачено времени {time.time() - start_time:.2f}")
