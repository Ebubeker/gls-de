import scrapy
import json
from ..middle import postalData


class GenspiderSpider(scrapy.Spider):
    name = 'genspider'
    allowed_domains = ['api.gls-pakete.de']
    index = 1
    start_urls = ['https://api.gls-pakete.de/parcelshops?version=3&coordinates=50.88246,8.91596&distance=10']
    usedLongLat = []

    def parse(self, response):
        firstResults = json.loads(response.body)
        results = firstResults['shops']
        print(postalData[1]['Postal_Code'])
        for result in results:
            address = result['address']
            coordinates = address['coordinates']
            longitude = coordinates['longitude']
            latitude = coordinates['latitude']
            name = address['name']
            state = 1

            if(GenspiderSpider.usedLongLat):
                for used in GenspiderSpider.usedLongLat:
                    if(used['longitute'] == float(longitude) and used['latitude'] == float(latitude)):
                        state = 0

            if(state == 1):
                dictToAdd = {
                    "longitute": float(longitude),
                    "latitude": float(latitude)
                }

                GenspiderSpider.usedLongLat.append(dictToAdd)

                yield {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [float(longitude), float(latitude)]
                    },
                    "properties": {
                        "name": name
                    }
                }


        next_link = 'https://api.gls-pakete.de/parcelshops?version=3&coordinates=' + str(postalData[GenspiderSpider.index]['Latitude']) + ',' + str(postalData[GenspiderSpider.index]['Longitude']) + '&distance=10'

        if GenspiderSpider.index < 16477:
            GenspiderSpider.index += 1
            print(GenspiderSpider.index)
            yield response.follow(next_link, callback=self.parse)
