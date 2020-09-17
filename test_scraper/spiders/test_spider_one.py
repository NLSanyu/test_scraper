import os
import scrapy
from dotenv import load_dotenv
load_dotenv()


class TestSpiderOne(scrapy.Spider):
    name = "test_one"
    start_urls = [
        os.environ.get("site_url_1")
    ]

    def parse(self, response):
        for property_item in response.css('div.property-card'):
            yield {
                'external_link':
                    property_item.css('a.property-card__link::attr(href)').get(),
                'title':
                    property_item.css('h4.property-card__title::text').get(),
                'square_meters':
                    property_item.css('span.property-card__feature::text')[0].get(),
                'room_count':
                    property_item.css('span.property-card__feature::text')[1].get(),
                'rent':
                    property_item.css('span.property-card__price::text').get()
            }
