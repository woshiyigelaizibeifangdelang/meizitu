# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from meizitu.items import MeizituItem
import os


class MeiziSpider(CrawlSpider):
    name = 'meizi'
    allowed_domains = ['www.eastbay.com']
    start_urls = ['https://www.eastbay.com/_-_/keyword-mens+adidas+harden+sgoes']
    # nes = r'\/:"|*?<>'
    # headers={
    #     'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 68.0.3440.75Safari /537.36'
    # }



    rules = (
        Rule( LinkExtractor(restrict_css='.endeca_pagination > a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):


        # print(1)

        title = response.css('.product_title::text').extract()
        price = response.css('.price::text').extract()
        urls = response.css('#endeca_search_results > ul > li> a::attr(href)').extract()
        k = 0
        # print(2)
        while k < len(urls):
            url = urls[k]
            yield scrapy.Request(url=url,callback=self.downss,meta={'title':title[k],'price':price[k]})
            k += 1
        # name = response.css('#pins img::attr(alt)').extract()
        # newname = name+'.'+url.split('.')[-1]
        # n=0
        # while n< len(url):
        #     newname = name[n] + '.' + url[n].split('.')[-1]
        #     print(url[n])
        #     yield scrapy.Request(url=url[n],  callback=self.downss, meta={'name': newname})
        #     # yield scrapy.Request(url=item['image_src'], callback=self.down, meta={'name': newname})
        #     n+=1

    def downss(self, response):
        # print(4)
        item = MeizituItem()
        title = response.meta['title']
        price = response.meta['price']
        color = response.css('.attType_color::text').extract()[0]
        sku = response.css('#productSKU ::text').extract()[0]
        details = response.css('#pdp_description').extract()[0]



        item['title'] = title
        item['price'] = price
        item['color'] = color
        item['sku'] = sku
        item['details'] = details
        print(6)
        yield item
        # newpath = os.path.join( r'D:\妹子图\fengmian', response.meta['name'])
        # print('%s' % newpath)
        # try:
        #     with open( newpath, 'wb' ) as of :
        #         of.write(response.body)
        # except:
        #     print('原名%s' % newpath)
        #     k = 0
        #     while k < 9:
        #         if MeiziSpider.nes[k] in newpath:
        #             r = newpath.index(MeiziSpider.nes[k])
        #             newpath = newpath[0:r] + newpath[r + 1:]
        #             continue
        #         k += 1
        #     with open( newpath, 'wb' ) as of :
        #         of.write(response.body)
        #











