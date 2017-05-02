import scrapy

class QuotesSpider(scrapy.Spider):
    name = "imagewall"
    start_urls = [
    'https://en.wikipedia.org/wiki/File:German_National_Library_of_Science_and_Technology_TIB_university_library_Hannover_UB_Am_Welfengarten_1b_Nordstadt_Hannover_Germany_03.jpg',
    'https://commons.wikimedia.org/wiki/File:TIB_Logo_DE_325px.png',
    ]

class MyItem(scrapy.Item):

    # ... other item fields ...
    image_urls = scrapy.Field()
    images = scrapy.Field()
