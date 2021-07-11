import requests
import time
from multiprocessing import Manager
import threading

def get_url(url, dict):
    start_time = time.time()
    for r in url:
      object = requests.get(r)
    dict[url[0]] =  time.time() - start_time


if __name__ == "__main__":
    URLS = ['https://docs.python.org/', 'https://realpython.com/', 'https://kaggle.com/', 'https://github.com/',
            'https://www.coursera.org/', 'https://trello.com/', 'https://www.sciencedirect.com/',
            'https://www.youtube.com/', 'https://bachasoftware.com/']
    start_time_total = time.time()

    with Manager() as mn:
        l0 = mn.list(URLS[:3])
        l1 = mn.list(URLS[3:6])
        l2 = mn.list(URLS[6:9])
        dict = mn.dict()
        try:
            thread = []
            t1 = threading.Thread(target=get_url, args=[l0, dict])
            thread.append(t1)
            t2 = threading.Thread(target=get_url, args=[l1, dict])
            thread.append(t2)
            t3 = threading.Thread(target=get_url, args=[l2, dict])
            thread.append(t3)
            # thread = [Thread(target=get_url, args=(url, dict, )) for url in URLS]
            for t in thread:
              t.start()
            for t in thread:
              t.join()
            time_total = time.time() - start_time_total
            print("Total of thread: ", time_total)
            print("List time in url : ", dict)

        except:
            print("error")