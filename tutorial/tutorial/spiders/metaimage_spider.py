import scrapy

class QuotesSpider(scrapy.Spider):
    name = "metaimage"
    start_urls = [    'https://upload.wikimedia.org/wikipedia/commons/c/c3/German_National_Library_of_Science_and_Technology_TIB_university_library_Hannover_UB_Am_Welfengarten_1b_Nordstadt_Hannover_Germany_03.jpg',]

    def parse_item(self, response):
            loader = XPathItemLoader(item = ImageItem(), response = response)
            loader.add_xpath('image_urls', '//img/@src')

            return loader.load_item()
