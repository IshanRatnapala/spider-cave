# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Country(scrapy.Item):
    countryCode1 = scrapy.Field()
    countryCode2 = scrapy.Field()
    countryName = scrapy.Field()
    countryCapital = scrapy.Field()
    countryArea = scrapy.Field()
    countryPopulation = scrapy.Field()
    continent = scrapy.Field()
    postcodeTranslation = scrapy.Field()


class Postcode(scrapy.Item):
    countryCode1 = scrapy.Field()
    postcode = scrapy.Field()
    areaname = scrapy.Field()
    address1 = scrapy.Field()
    address2 = scrapy.Field()
    address3 = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
