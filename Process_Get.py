import requests
import time
from multiprocessing import Process

def get_url(url):
    object = requests.get(url)

if __name__ == "__main__":
    start_time_total = time.time()
    URLS = ['https://docs.python.org/', 'https://realpython.com/', 'https://kaggle.com/', 'https://github.com/',
            'https://www.coursera.org/', 'https://trello.com/', 'https://www.sciencedirect.com/',
            'https://www.youtube.com/', 'https://bachasoftware.com/']
    dict = {}
    try:

        for url in URLS:
            start_time = time.time()
            process = Process(target=get_url, args=[url])
            process.start()
            process.join()
            stop_time = time.time()
            dict[url] = stop_time - start_time
        time_total = time.time() - start_time_total
        print("Total of process: ", time_total)
        print("List time in url : ", dict)
    except:
        print("error")