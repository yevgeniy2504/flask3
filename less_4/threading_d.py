import argparse

import requests
import threading
import time
from synchronize_method import data_image, synchronize_download

parser = argparse.ArgumentParser(description="Парсер изображений")
parser.add_argument("--urls", default=data_image, nargs="+", help="список URL адресов для загрузке изображений")
args = parser.parse_args()
urls = args.urls
if not urls:
    urls = data_image


threads = []
start_time = time.time()

for img in urls:
    thread = threading.Thread(target=synchronize_download, args=["treads_", img])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"всего затрачено времени {time.time() - start_time:.2f}")
