import scrapy
import pgeocode
import requests
import json
import urllib
from pprint import pprint

class PostalcodesSpider(scrapy.Spider):
    name = 'postalCodes'
    allowed_domains = ['https://www.google.com/']
    start_urls = ['https://www.google.com/']
    nomi = pgeocode.Nominatim('de')

    def parse(self, response):
        print('commented')
        # url = 'https://parseapi.back4app.com/classes/Postal_Codes_Germany?limit=16477&keys=Postal_Code,Latitude,Longitude'
        # headers = {
        #     'X-Parse-Application-Id': 'uLFpqkB30ZlsDBLVGEFinxLp1qz7XrtZDkkj69qG',
        #     'X-Parse-Master-Key': 'w30JMT1stROFiW95WuTKupgUSOcXC4UOMXz60Z2D'
        # }
        # data = json.loads(requests.get(url, headers=headers).content.decode('utf-8'))
        # # print(data)
        # results = data["results"]
        #
        # for result in results:
        #     yield result


