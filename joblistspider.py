'''scrape all the content in the jobberman website '''


import os
import scrapy
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess
#from ..jobs_items import JobsItemsSpider


class JobSpider(scrapy.Spider):
    
    name = 'jobberman'
    
    page_number =  2
    
    
    start_urls = ['https://www.jobberman.com/jobs?page=']
    
    
    
        
        
    def parse(self,response):
        jobs_items = JobsItemsSpider()
        
        jobs = response.xpath('//article[@class ="search-result "]/text()').extract()
        
        
        name = response.xpath('//h3/text()').extract()
        link = response.xpath('//a[@class="search-result__job-title metrics-apply-now "]/@href').extract()
        location = response.xpath('//div[@class="search-result__location"]/text()').extract()
        types = response.xpath('//span[@class="search-result__job-type"]/text()').extract()
        salary = response.xpath('//div[@class="search-result__job-salary"]/text()').extract()
        timestamp = response.xpath('//div[@class="label--new margin-left--10" title="]/text()').extract()
        job_function = response.xpath('//div[@class="padding-lr-10 gutter-flush-under-lg"]/text()').extract()
        summary =  response.xpath('//p/text()').extract()
        
        
        jobs_items['name'] = name
        jobs_items['link'] = link
        jobs_items['locationn'] = location
        jobs_items['types'] = types
        jobs_items['salary'] = salary 
        jobs_items['timestamp'] = timestamp
        jobs_items['job_function'] = job_function
        jobs_items['summary'] = summary     
        
        
        
        yield jobs_items   
        
        
        next_page ='https://www.jobberman.com/jobs?page=' + str(JobSpider.page_number)   
        if JobSpider.page_number <= 56:
            JobSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)
    

    
    
    
    
#main driver #
if __name__ == '__main__':
   pass