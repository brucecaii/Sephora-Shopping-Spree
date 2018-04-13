# -*- coding: utf-8 -*-
import scrapy
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class SephoraSpider(scrapy.Spider):
    name = 'precedent_id_spider'
    allowed_domains = ['sephora.com']
    start_urls = ['https://www.sephora.com/?country_switch=ca&lang=en']

    def __init__(self):
        self.driver = webdriver.Chrome()
        # Let the spree begins...

    def parse(self, response):
        # Open browser and load the url
        self.driver.get(response.url)
        self.driver.find_element_by_id('signin_username')
        sleep(30)