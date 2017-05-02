import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://en.wikipedia.org/wiki/German_National_Library_of_Science_and_Technology',
    ]


    def parse(self, response):
        for quote in response.css('title'):
            yield {
                'title': quote.css('title::text').extract_first(),

            }
