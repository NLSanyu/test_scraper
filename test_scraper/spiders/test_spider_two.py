import os
import scrapy
from dotenv import load_dotenv
load_dotenv()


class TestSpiderTwo(scrapy.Spider):
    name = "test_two"
    start_urls = [
        os.environ.get("site_url_2")
    ]

    def parse(self, response):
        for property_item in response.css('div.listing-houses'):
            yield {
                'external_link':
                    property_item.css('a.houses-url::attr(href)').get(),
            }
