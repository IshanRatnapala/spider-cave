import scrapy

from opscraper.items import Country, Postcode

class PostcodesSpider(scrapy.Spider):
    name = 'postcodes'
    start_urls = ['http://www.datapedia.co/postcodes']

    def parse(self, response):
        for href in response.css('.col-hold a::attr(href)').extract(): #remove first
            print '1 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
            print href
            print response.urljoin(href)
            yield scrapy.Request(response.urljoin(href), callback=self.parseCountry)
            return

    def parseCountry(self, response):
        countryUrl = response.css('.content-block a::attr(href)').extract_first()
        print '2 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
        print response.urljoin(countryUrl)
        yield scrapy.Request(response.urljoin(countryUrl), callback=self.parsePostcodes)

    def parsePostcodes(self, response):
        postcodeUrl = response.css('.col-hold a::attr(href)').extract_first() #remove first
        print '3 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
        print response.urljoin(postcodeUrl)
        yield scrapy.Request(response.urljoin(postcodeUrl), callback=self.parsePostcode)

    def parsePostcode(self, response):
        postcode = response.css('.table-responsive td::text')[2].extract()

        country = Country()
        country['name'] = 'name'

        print '4 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
        print postcode
