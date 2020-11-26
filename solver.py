import requests
import pandas as pd
from bs4 import BeautifulSoup
from dateutil.parser import parse
from time import sleep, time
from random import randint
import re
from IPython.core.display import clear_output
from warnings import warn
import numpy as np
from selenium import webdriver 
import cv2 
import pytesseract
from PIL import Image
import inputs

def is_captcha_page(soup,captcha_text=inputs.captcha_text):
    page_info=soup.find('font',attrs={'class':"pagebodybold"})
    if page_info!=None and captcha_text in page_info.text:
        return True
    return False

def solve_captcha(company_link):
    driver = webdriver.Firefox('/home/udit/projects/chromiumm')
    driver.get(company_link)
    element = driver.find_element_by_id("imgCaptcha")
    element.screenshot('final.png')
    img = cv2.imread('final.png')
    captcha=inputs.captcha_solver(img)
    
    captcha=re.sub(r'\W+', '', captcha)
    captcha_input = driver.find_element_by_xpath("//input[@id ='txtCaptcha']") 
    captcha_input.send_keys(captcha) 

    # submit button clicked
    driver.find_element_by_xpath("//input[@id ='btnRegiser']").click()
    html = driver.page_source
    soup = BeautifulSoup(html)
    driver.close()
    return soup