from selenium import webdriver
import time
import urllib.request
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def fetch_google_and_download_image(query):

    option = Options()
    option.headless = True
    browser = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe', options=option)
    browser.get('https://www.google.com/')
    search =  browser.find_element_by_name('q')
    search.send_keys(query, Keys.ENTER)
    element = browser.find_element_by_link_text('Imagens')
    element.get_attribute('href')
    element.click()

    images = browser.find_element_by_id('islrg')

    time.sleep(2)
    images.find_element_by_tag_name('a').click()
    time.sleep(2)

    element = browser.find_element_by_class_name('OUZ5W')
    image = element.find_elements_by_tag_name('img')


    srcs = []
    for i in image[:2]:
        breakpoint()
        src = i.get_attribute('src')
        srcs.append(src)
    print(srcs)
    # make_file_if_not_exists()
    # download_image(query, src)
    # browser.quit()

def make_file_if_not_exists():
    try:
        os.mkdir('downloads')
    except FileExistsError:
        pass

def download_image(query, src):
    try:
        if src != None:
            src  = str(src)    
            urllib.request.urlretrieve(src, os.path.join('downloads',''.join(query.split())+'.jpg'))
        else:
            raise TypeError
    except TypeError:
        print('fail')

    

if __name__=='__main__':
    fetch_google_and_download_image('Michael Jackson moonwalk')