import scrapy



class JobsItemsSpider(scrapy.Item):

    #define the field for your items here like :
    # name =  scrapy.Field()
    
    name = scrapy.Field()
    link = scrapy.Field()
    location = scrapy.Field()
    types = scrapy.Field()
    salary = scrapy.Field()
    timestamp = scrapy.Field()
    job_function = scrapy.Field()
    summary = scrapy.Field()
    pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # name = 'jobs_items'
    # allowed_domains = ['jobberman.com']
    # start_urls = ['http://jobberman.com/jobs']

    # def parse(self, response):
    #     self.log('I just visited:' + response.url)
    #     pass
    #     # yield{
            
        #     'name' : response.xpath('//h3/text()').get()
        #     'link' : response.xpath('//a[@class="search-result__job-title metrics-apply-now "]/@href').get()
        #     'location' : response.xpath('//div[@class="search-result__location"]/text()').get()
        #     'types' : response.xpath('//span[@class="search-result__job-type"]/text()').get()
        #     'salary': response.xpath('//div[@class="search-result__job-salary"]/text()').get()
        #     'timestamp' : response.xpath('//div[@class="label--new margin-left--10" title="]/text()').get()
        #     'job_function':response.xpath('//div[@class="padding-lr-10 gutter-flush-under-lg"]/text()').get()
        #     'summary' :  response.xpath('//h3/text()').get()
        # }pass
