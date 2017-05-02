import scrapy

class QuotesSpider(scrapy.Spider):
    name = "title"
    start_urls = ['https://en.wikipedia.org/wiki/German_National_Library_of_Science_and_Technology',
    ]

    def parse(self, response):
        for title in response.css('title'):
            yield {
                'title': title.css('title::text').extract_first(),
            }
