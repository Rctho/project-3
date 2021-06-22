from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager


# Declare Dependencies 
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import requests
import warnings
import pandas as pd
import os

# warnings.filterwarnings('ignore')

## define a global variable to store the data
news_info_dict = {}

## Set up Splinter
def setup_splinter():
  # @NOTE: Path to the local chromedriver
  # executable_path = {"executable_path": "C:\xx\Users\\charm\\Desktop\chromedriver"}
  executable_path = {'executable_path': ChromeDriverManager().install()}
  browser = Browser('chrome', **executable_path, headless=False)
  return browser

##--------------------
## Mars News from NASA
##--------------------
def scrape_cnn_news():
  # Set up Splinter
  browser = setup_splinter()

  # Visit CNN News Site n 2020 Presidential Result Page that to be scraped
  news_url = 'https://www.cnn.com/election/2020/results/president/'
  browser.visit(news_url)
  time.sleep(1)

  # Scrape page into Soup
  news_html = browser.html
  news_soup = bs(news_html, "html.parser")
  # list_text_all = news_soup.find_all('div', class_='list_text')
  list_text_all = news_soup.find_all('h2', class_ = 'lciBzu')
  ## scrape the first result from the ResultSet (list_text_all):
  content_title = list_text_all[0]
  news_title = content_title.text.strip()


  # content_subtitle = list_text_all[0].find('div', class_ = 'bUXXrl')
  news_subtitle_text_all = news_soup.find_all('p', class_ = 'bUXXrl')
  news_substitle_text = news_subtitle_text_all[0]
  news_substitle = news_substitle_text.text.strip()
  
  # news_paragraph = list_text_all[0].find('p', class_ = 'udXIW')
  news_paragraph_text_all = news_soup.find_all('p', class_ = 'udXIW')
  news_paragraph_text = news_paragraph_text_all[0]
  news_p = news_paragraph_text.text.strip()

  ## Save the data to mars_info
  news_info_dict['news_title'] = news_title
  news_info_dict['news_subtitle'] = news_substitle
  news_info_dict['news_paragraph'] = news_p

  browser.quit()
  return news_info_dict
