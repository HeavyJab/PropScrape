# -*- coding: utf-8 -*-
import scrapy

class SeekSpider(scrapy.Spider):
    name = 'seek'
    start_urls = ['https://www.seek.com.au/data-scientist-jobs/in-All-Melbourne-VIC']

    def parse(self, response):
        for url in response.xpath('//div[@data-sol-meta]/article/span/div[@href]/@href').extract():
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse)

        ads = {}
        header = response.xpath('//section[@aria-labelledby="jobInfoHeader"]//text()').extract()
        ads['job_title'] = response.xpath('//span[@data-automation="job-detail-title"]//text()').extract_first()
        ads['recruiter'] = response.xpath('//span[@data-automation="advertiser-name"]//text()').extract_first()
        ads['job_date'] =  response.xpath('//dd[@data-automation="job-detail-date"]//text()').extract_first()
        ads['job_type'] = response.xpath('//dd[@data-automation="job-detail-work-type"]//text()').extract_first()
        ads['job_desc'] = response.xpath('//div[@data-automation="mobileTemplate"]//text()|ul//text()').extract()
        yield ads
