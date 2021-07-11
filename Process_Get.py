import requests
import time
from multiprocessing import Process, Manager


def get_url(url, dict):
    start_time = time.time()
    for r in url:
      object = requests.get(r)

    dict[url[0]] = time.time() - start_time

if __name__ == "__main__":
    URLS = ['https://docs.python.org/', 'https://realpython.com/', 'https://kaggle.com/', 'https://github.com/',
            'https://www.coursera.org/', 'https://trello.com/', 'https://www.sciencedirect.com/',
            'https://www.youtube.com/', 'https://bachasoftware.com/']
    with Manager() as mn:

        l0 = mn.list(URLS[:3])
        l1 = mn.list(URLS[3:6])
        l2 = mn.list(URLS[6:9])

        start_time_total = time.time()
        dict = mn.dict()
        try:
            process = [Process(target=get_url, args=[url, dict, ]) for url in [l0, l1, l2]]
            for p in process:
                p.start()
            for p in process:
                p.join()
                p.close()
            time_total = time.time() - start_time_total
            print("Total of process: ", time_total)
            print("List time in url : ", dict)
        except:
            print("error")