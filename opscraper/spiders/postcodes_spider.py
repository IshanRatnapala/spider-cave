import scrapy

from opscraper.items import Country, Postcode

class PostcodesSpider(scrapy.Spider):
    name = 'postcodes'
    start_urls = ['http://www.datapedia.co/postcodes']

    def parse(self, response):
        for href in response.css('.col-hold a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(href), callback=self.parseCountry)
            return

    def parseCountry(self, response):
        countryUrl = response.css('.content-block a::attr(href)').extract_first()
        yield scrapy.Request(response.urljoin('countryUrl'), callback=self.parsePostcodes)

    def parsePostcodes(self, response):
        for postcodeUrl in response.css('.col-hold a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(postcodeUrl), callback=self.parsePostcode)

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parsePostcodes)

    def parsePostcode(self, response):
        def getText(row):
            return response.xpath('//div[@class="tbl"]//tr[' + str(row) + ']/td[2]//text()').extract_first()

        country = Country()
        country['countryCode1'] = getText(9)
        country['countryCode2'] = getText(10)
        country['countryName'] = getText(11)
        country['countryCapital'] = getText(12)
        country['countryArea'] = getText(13)
        country['countryPopulation'] = getText(14)
        country['continent'] = getText(15)
        country['postcodeTranslation'] = getText(8)

        postcode = Postcode()
        postcode['countryCode1'] = getText(9)
        postcode['postcode'] = getText(1)
        postcode['areaname'] = getText(2)
        postcode['address1'] = getText(3)
        postcode['address2'] = getText(4)
        postcode['address3'] = getText(5)
        postcode['latitude'] = getText(6)
        postcode['longitude'] = getText(7)

        return {
            'country': country,
            'postcode': postcode
        }
