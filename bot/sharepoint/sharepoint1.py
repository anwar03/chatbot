import requests
import re
import json
import pdfkit
import html
import os
from django.conf import settings
from bs4 import BeautifulSoup
from shareplum import Office365
from shareplum import Site
from shareplum import folder
from shareplum.request_helper import get, post
from shareplum.site import Version

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import chromedriver_binary


class ShareData1:
    def __init__(self):
        self._username = 'YogyaBot@yogyassl.onmicrosoft.com'
        self._password = 'Chatbot2020%'
        self._site = 'https://yogyassl.sharepoint.com'
        self._url = 'https://yogyassl.sharepoint.com/sites/YogyaDemo'
        self._session = requests.Session()
        self.authcookie = Office365(
            self._site,
            username=self._username,
            password=self._password).GetCookies()
        self._session.cookies = self.authcookie
        self.site = Site(
            self._url,
            version=Version.v365, authcookie=self.authcookie
            )

        # print(self.authcookie)

    def site_data(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        HOME_DIR = os.path.realpath(os.path.join(BASE_DIR, '..'))
        ASPX_DATA_URL = os.path.join(HOME_DIR, 'aspx/')
        HTML_DATA_URL = os.path.join(HOME_DIR, 'html/')
        PDF_DATA_URL = os.path.join(HOME_DIR, 'pdf/')

        # html_path = os.path.join(HTML_DATA_URL, html_name)
        # pdf_path = os.path.join(PDF_DATA_URL, pdf_name)
        url = ASPX_DATA_URL+"Events.aspx"
        print(url)
        # create a new Firefox session
        self.driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
        # self.driver.add_cookie(self.authcookie)
        self.driver.implicitly_wait(30)
        self.driver.get(url)

        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        d = open("aspx/events.html", 'w')
        d.write(soup.prettify())
        d.close()
        print("done")
