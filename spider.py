from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

class Pregunta(Item):
        id = Field()
        pregunta = Field()

class StackOverflowSpider(Spider):
        name = "MiPrimerSpider"
        start_urls = ['https://www.minsal.cl/nuevo-coronavirus-2019-ncov/casos-confirmados-en-chile-covid-19/']

        def parse(self, response):
            sel = Selector(response)
            preguntas = sel.xpath('//div[@class="contenido"]/table/tbody/tr')

            # Iterar sobre todas las preguntas
            for i, elem in enumerate(preguntas):
                item = ItemLoader(Pregunta(), elem)
                item.add_xpath('pregunta', './/td/text()')
                item.add_value('id', i)

                yield item.load_item()
