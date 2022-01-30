from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
import csv


class GithubCrawler(CrawlSpider):
    name = "gitcrawler"
    allowed_domains = ['github.com']
    # start_urls = ['https://github.com/3-amigos/la-morenita/tree/master']
    custom_settings = {
        'DEPTH_LIMIT': 3,
    }

    rules = (
        Rule(LinkExtractor(allow=r'tree/master/src.*'), follow=True),
        Rule(LinkExtractor(allow=r'src.*'), callback='parse_page'),
    )

    csvreader = None
    urls = []
    repos = []

    def __init__(self, filename=None, *args, **kwargs):
        if filename:
            with open(filename, 'r') as f:
                csvreader = csv.reader(f)
                # header = next(csvreader)
                for row in csvreader:
                    self.urls.append('https://github.com/' + row[0] + '/tree/master')
                    self.repos.append(row[0])
                self.start_urls = self.urls
        super(GithubCrawler, self).__init__(*args, **kwargs)

    def parse_page(self, response):
        '''tag_selector = response.xpath('//a')
        for tag in tag_selector:
            link = tag.xpath('@href').extract_first()
            # print(link)
            if link is not None and (str(link).find('src/test') != -1):
                req = response.request
                req_headers = req.__dict__['headers']
                referer_url = req_headers['Referer'].decode('utf-8')
                with open('data.txt', 'a') as f:
                    f.write(str(referer_url) + '\n')
                break'''

        req = response.request
        req_headers = req.__dict__['headers']
        referer_url = req_headers['Referer'].decode('utf-8')

        with open("watchlist_intellij.txt", "r") as f:
            watched_set = set(f.read().splitlines())

        with open('watchlist_intellij.txt', 'a') as f:
            splits = str(referer_url).split('/')
            watched_repo = splits[3] + '/' + splits[4]
            if watched_repo not in watched_set:
                f.write(watched_repo + '\n')

        if referer_url is not None and (str(referer_url).find('src/test') != -1):
            portions = str(referer_url).split('/')
            repo = portions[3] + '/' + portions[4]

            with open("data_intellij.txt", "r") as f:
                line_set = set(f.read().splitlines())

            with open('data_intellij.txt', 'a') as f:
                if repo in self.repos and repo not in line_set:
                    f.write(repo + '\n')
