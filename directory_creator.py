import os


# this is the first task of MySpider
# each website you crawl, the crawler creates a separate folder
# creating a function that creates a folder directory per website/app
# creates a folder only if one from the path does not exist
def create_new_folder(directory):
    if not os.path.exists(directory):
        print('Create new directory: ' + directory)
        os.makedirs(directory)


# This creates the data for directory which creates 2 separate files ( URL queue, and crawled) for tracking
# create new queue and crawled files
def create_data_files(directory_name, base_url):
    queue = directory_name + '/queue.txt'
    crawled = directory_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# creates a new file, using good write practices
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# add data onto existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Clear the contents of a file
def clear_file_contents(path):
    with open(path, 'w'):
        pass


# Store data in a set (using 2 different functions)to make more efficient and secure data from loss incidences
# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results


# Iterate through a set, each item will be a new line in the file
def set_to_file(links, file):
    clear_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)
