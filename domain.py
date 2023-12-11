from urllib.parse import urlparse


# responsible for extracting given domain names (network location) only and not external links

# Get domain name (ex: example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return  results[-2] + '.' + results[-1]
    except:
        return ''


# Get sub domain name function (ex: name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
    