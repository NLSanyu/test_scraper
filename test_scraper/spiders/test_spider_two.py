import scrapy

class TestSpiderTwo(scrapy.Spider):
    name = "test_two"
    start_urls = [
        "https://www.lemoo.nl/woningaanbod?status=rent"
    ]
    
    def parse(self, response):
        for property_item in response.css('div.listing-houses'):
            yield {
                external_link: property_item.css('a.houses-url::attr(href)').get(),
            }
