from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class CcrawlexSpider(CrawlSpider):
    name = 'cCrawlEx'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/ClickerMonkey/TrieHard/tree/master']

    custom_settings = {
        'DEPTH_LIMIT': 1,
    }

    rules = (
        Rule(LinkExtractor(allow=r'tree/master.*'), follow=True),
        Rule(LinkExtractor(allow=r'master.*'), callback='parse_item'),
    )

    def parse_item(self, response):
        print(response)