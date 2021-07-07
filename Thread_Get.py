import requests
import time
from multiprocessing import Manager
import threading


def get_url(url, dict):
    start_time = time.time()
    object = requests.get(url)
    dict[url] = time.time() - start_time


if __name__ == "__main__":
    URLS = ['https://docs.python.org/', 'https://realpython.com/', 'https://kaggle.com/', 'https://github.com/',
            'https://www.coursera.org/', 'https://trello.com/', 'https://www.sciencedirect.com/',
            'https://www.youtube.com/', 'https://bachasoftware.com/']
    with Manager() as mn:
        start_time_total = time.time()
        dict = mn.dict()
        try:
            thread = []
            for url in URLS:
              t = threading.Thread(target=get_url, args=(url, dict))
              thread.append(t)
            for t in thread:
              t.start()
            for t in thread:
              t.join()
              if t.isAlive():
                t.setDaemon(True)
            time_total = time.time() - start_time_total
            print("Total of thread: ", time_total)
            print("List time in url : ", dict)

        except:
            print("error")