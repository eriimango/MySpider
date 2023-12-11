from urllib import urlopen
from link_finder import LinkFinder
from directory_creator import *


# Takes the queue and crawl file to share amongst various amounts of spiders
class Spider:

    # Class variable shared among all spider instances
    directory_name = ''
    base_url = ''
    domain_name = ''
    queue_txt_file = ''
    crawled_txt_file = ''
    queue = set()
    crawled = set()

    def __int__(self, directory_name, base_url, domain_name):
        Spider.directory_name = directory_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_txt_file = Spider.directory_name + '/queue.txt'
        Spider.crawled_txt_file = Spider.directory_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First Spider -', Spider.base_url)

    @staticmethod
    def boot():
        create_new_folder(Spider.directory_name)
        create_data_files(Spider.directory_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_txt_file)
        Spider.crawled = file_to_set(Spider.crawled_txt_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' is now crawling ' + page_url)
            print('Queue: ' + str(len(Spider.queue)) + ' | Crawled: ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    # Convert html bytes to human-readable strings (utf-8)
    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except:
            print('ERROR: Can not crawl page!')
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_txt_file)
        set_to_file(Spider.crawled, Spider.crawled_txt_file)






