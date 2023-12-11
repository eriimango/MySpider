import threading
from queue import Queue
from spider import Spider
from domain import *
from directory_creator import *

DIRECTORY_NAME = ''
HOMEPAGE = ''
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = DIRECTORY_NAME + '/queue.txt'
CRAWLED_FILE = DIRECTORY_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(DIRECTORY_NAME, HOMEPAGE, DOMAIN_NAME)


# Create worker(spiders) threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.currentThread().name, url)
        queue.task_done()


# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# Heart of program: checks if there are items in the queue, if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links are in the queue to be crawled.')
        create_jobs()


create_workers()
crawl()
