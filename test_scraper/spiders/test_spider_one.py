import scrapy

class TestSpiderOne(scrapy.Spider):
    name = "test_one"
    start_urls = [
        "https://www.laforet.com/louer/rechercher?next=100000"
    ]
    
    def parse(self, response):
        for property_item in response.css('div.property-card'):
            yield {
                external_link: property_item.css('a.property-card__link::attr(href)').get(),
                title: property_item.css('h4.property-card__title::text').get(),
                square_meters: property_item.css('span.property-card__feature::text')[0].get(),
                room_count: property_item.css('span.property-card__feature::text')[1].get(),
                rent: property_item.css('span.property-card__price::text').get()
            }
        next_page = response.css('a.next-posts-link::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)