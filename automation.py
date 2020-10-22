from bs4 import BeautifulSoup as soup
import urllib.request
import os, sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# import browser_info
from time import sleep
import random
import json
import csv
import requests, re
from datetime import datetime

class Automation:
    def __init__(self):
        self.driver = ""
        self.path_to_chromedriver = "C:/Users/Administrator/Desktop/bot_selenium/chromedriver.exe"
        self.browser_url = "127.0.0.1:"
        self.target_url = "https://app.pinetool.ai/attendee/events/965/people"

    def driver_startup(self, browser_port):
        chrome_options = Options()
        # PROXY = "66.70.224.81:3129"
        chrome_options.add_argument("--headless")
        # chrome_options.add_argument('--proxy-server={}'.format(PROXY))
        chrome_options.add_experimental_option("debuggerAddress", self.browser_url + str(browser_port))
        self.driver = webdriver.Chrome(self.path_to_chromedriver, options=chrome_options)

    def main(self):
        print(" here is automation called")
        # try:
        browser_port = 9235
        self.driver_startup(browser_port)
        self.driver.maximize_window()
        sleep(1)
        self.driver.get(self.target_url)
        sleep(4)
        # next_icon = self.driver.find_element_by_xpath('//*[@id="content-container"]/div[2]/div[3]/span')
        # next_icon.click()
        # sleep(1)
        # next_icon.click()
        sleep(2)
        page_num =8

        filename = "data1.csv"
        #writing to csv file  
        with open(filename, 'w', encoding='utf-8') as csvfile:  
            csvwriter = csv.writer(csvfile)
            while True:
                print("page", page_num)
                list_of_people_element = self.driver.find_elements_by_xpath('//*[@id="content-container"]/div[1]/table[2]/tbody/tr')
                print("42", len(list_of_people_element))
                length = len(list_of_people_element)
                #msg_content = "Hi, I am the CEO and Founder of a DevSecOps startup called Sken.ai. Sken.ai is one tool to do all types of security scans. Sken adds SAST, DAST and other security testing to the SCA that you already get with Snyk. Sken uses open source scanners and that makes it 10x affordable. It is easy to use and very DevOps friendly. You can visit www.sken.ai to sign up for free. If you would like to have a quick demo of sken, you can book a time using https://calendly.com/sundar_sken/30min Thanks. Sundar"

                
                msg_content2 = "I am the CEO and Founder of a DevSecOps startup called Sken.ai."
                msg_content3 = "Sken.ai is one tool to do all types of security scans. Sken adds SAST, DAST and other security testing to the SCA that you already get with Snyk. Sken uses open source scanners and that makes it 10x affordable. It is easy to use and very DevOps friendly."
                msg_content4 = "You can visit www.sken.ai to sign up for free. If you would like to have a quick demo of sken, you can book a time using https://calendly.com/sundar_sken/30min"
                msg_content5 = "Thanks"
                msg_content6 = "Sundar"
                for i in range(length):
                    msg_content1 = "Hi "
                    print("person", i)
                    name = ''
                    try:
                        name = self.driver.find_element_by_xpath('(//*[@id="content-container"]/div[1]/table[2]/tbody/tr)[' + str(i + 1) + ']//div[@class="avatar-label"]/a').text
                        
                    except:
                        pass
                    print("name")
                    
                    title = ''
                    try:
                        title = self.driver.find_element_by_xpath('(//*[@id="content-container"]/div[1]/table[2]/tbody/tr)[' + str(i + 1) + ']/td[1]/div/div[2]/div').text
                        print("title")
                    except:
                        pass
                    print("tit")
                    company = ''
                    try: 
                        company = self.driver.find_element_by_xpath('(//*[@id="content-container"]/div[1]/table[2]/tbody/tr)[' + str(i + 1) + ']//div[@class="company"]/a').text
                        print("company")
                    except:
                        pass
                    print("cpm", company)
                    # save in the csv
                    fields = [name, title, company]
                    csvwriter.writerow(fields)  

                    # msg_content1 = msg_content1 + name
                    # # list_of_people_element[i].find_element_by_class_name('avatar-label').click()
                    # self.driver.find_element_by_xpath('(//*[@id="content-container"]/div[1]/table[2]/tbody/tr)[' + str(i + 1) + ']//div[@class="avatar-label"]/a').click()
                    # sleep(3)
                    # send_btn_element = self.driver.find_element_by_xpath('//*[@id="page"]/div/div[2]/div[1]/div[1]/div[1]/div[2]/a[1]')
                    # send_btn_element.click()
                    # sleep(1)
                    # msg_textbox = self.driver.find_element_by_xpath('//*[@id="chat-widget"]/div/div/div[3]/div/textarea')
                    # msg_textbox.send_keys(msg_content1)
                    # sleep(1)
                    # msg_textbox.send_keys(Keys.SHIFT,'\n')
                    # sleep(1)
                    # msg_textbox.send_keys(Keys.SHIFT,'\n')
                    # sleep(1)
                    # msg_textbox.send_keys(msg_content2)
                    # sleep(1)
                    # msg_textbox.send_keys(Keys.SHIFT,'\n')
                    # msg_textbox.send_keys(Keys.SHIFT,'\n')
                    # sleep(1)
                    # msg_textbox.send_keys(msg_content3)
                    # sleep(1)
                    # msg_textbox.send_keys(Keys.SHIFT,'\n')
                    # msg_textbox.send_keys(Keys.SHIFT,'\n')
                    # sleep(1)
                    # msg_textbox.send_keys(msg_content4)
                    # sleep(1)
                    # msg_textbox.send_keys(Keys.SHIFT,'\n')
                    # msg_textbox.send_keys(Keys.SHIFT,'\n')
                    # sleep(1)
                    # msg_textbox.send_keys(msg_content5)
                    # sleep(1)
                    # msg_textbox.send_keys(Keys.SHIFT,'\n')
                    # msg_textbox.send_keys(Keys.SHIFT,'\n')
                    # sleep(1)
                    # msg_textbox.send_keys(msg_content6)
                    # sleep(1)

                    # send_icon = self.driver.find_element_by_xpath('//*[@id="chat-widget"]/div/div/div[3]/div/div/i')
                    # send_icon.click()
                    # sleep(2)
                    # close_icon = self.driver.find_element_by_xpath('//*[@id="chat-widget"]/div/div/div[1]/i')
                    # close_icon.click()
                    # sleep(1)
                    # back_icon = self.driver.find_element_by_xpath('//*[@id="page"]/div/div[1]/div/h1/div')
                    # back_icon.click()
                    # sleep(2)

                next_icon = self.driver.find_element_by_xpath('//*[@id="content-container"]/div[2]/div[3]/span')
                next_icon.click()
                page_num = page_num + 1
                sleep(1)



        

if __name__ == '__main__':
    cashbot = Automation()
    cashbot.main()
