# -*- coding: utf-8 -*-
import scrapy
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import win32api


class SephoraSpider(scrapy.Spider):
    name = 'precedent_id_spider'
    allowed_domains = ['sephora.com']
    start_urls = ['https://www.sephora.com/basket']

    def __init__(self):
        sleep(5)
        self.driver = webdriver.Chrome()
        try:
            with open('info.json', 'r+') as account:
                account_info = json.load(account)
                self.email = account_info['email']
                self.password = account_info['password']
                self.promotion_code = account_info['promotion_code']
                self.driver.get('https://www.sephora.com/?country_switch=ca&lang=en')
                self.driver.find_element_by_id('signin_username').send_keys(self.email)
                self.driver.find_element_by_id('signin_password').send_keys(self.password, Keys.ENTER)
                sleep(2)
        except BaseException:
            print('No account is set.')
            exit()

    def parse(self, response):
        # Open browser and load the url
        self.driver.get(response.url)
        error = True
        while error:
            sleep(5)
            self.driver.find_element_by_css_selector('body.css-aitllj div.css-68zqxa:nth-child(1) div.css-5gcev7 div.css-1gxp9ne:nth-child(1) div.css-a5d2qf div.css-1gj9jiq div.css-1obc678:nth-child(1) div:nth-child(2) form.css-1u6aw16:nth-child(2) div.css-nil div.css-13azwyo > input.css-1avl08g').send_keys(self.promotion_code, Keys.ENTER)
            sleep(2)
            error = self.driver.find_element_by_class_name('css-1n8z65d')
            if (error):
                self.driver.refresh()
        win32api.MessageBox(0, 'Ready')


