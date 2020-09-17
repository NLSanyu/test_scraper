import scrapy

class TestSpider(scrapy.spider):
    name = "test"
    start_urls = [
        "https://www.lemoo.nl/woningaanbod?status=rent",
        "https://www.laforet.com/louer/rechercher?next=100000"
    ]
    
    def parse(self, response):
        pass
