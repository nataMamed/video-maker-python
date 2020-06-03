from state import load_content, save_content
import json
from selenium import webdriver
import time
import urllib.request
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class Image:

    def __init__(self):
        self.content = load_content()

    
    def fetch_google_and_download_image(self, query):

        option = Options()
        option.headless = True
        browser = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe', options=option)
        browser.get('https://www.google.com/')
        search =  browser.find_element_by_name('q')
        search.send_keys(query, Keys.ENTER)
        element = browser.find_element_by_link_text('Imagens')
        element.get_attribute('href')
        element.click()
        time.sleep(1)
        images = browser.find_element_by_id('islrg')
        time.sleep(2)
        images.find_element_by_tag_name('a').click()
        time.sleep(2)
        element = browser.find_element_by_class_name('OUZ5W')
        image = element.find_element_by_tag_name('img')
        src = image.get_attribute('src')
        browser.quit()
        self.download_image(query, src)
        return src

    @staticmethod
    def make_file_if_not_exists():
        try:
            os.mkdir('content')
        except FileExistsError:
            pass

    @staticmethod
    def download_image(query, src):
        try:
            if src != None:
                src  = str(src)    
                urllib.request.urlretrieve(src, os.path.join('content',''.join(query.split())+'.jpg'))
            else:
                raise TypeError
        except TypeError:
            print('fail')

    def fetch_images_of_all_sentences(self):

        self.make_file_if_not_exists()

        search_term = self.content['userInput']['searchTerm']
        sentences = self.content['sentences']
        for sentence in sentences:
            query = f"{search_term} {sentence['keywords'][0]}"
            sentence['images'] = self.fetch_google_and_download_image(query)
            sentence['googleSearch'] = query

        self.content['sentences'] = sentences
        save_content(self.content)
        return sentences

        
if __name__=='__main__':
    c = Image()
    print(c.fetch_images_of_all_sentences())
"""
    def fetch_google_and_return_image_links(self, query):

        service = build("customsearch", "v1",
                developerKey=self.google_api_key)

        res = service.cse().list(
            q=query,
            cx=self.google_cse_id,
            searchType='image',
            num=2
        ).execute()

        if 'items' in res.keys():
            return res['items']
        return 
"""
"""
    def set_google_api_key_and_id(self):
        with open('credentials/google-search.json') as json_file:
            data = json.load(json_file)
            google_api_key = data['apiKey']
            google_cse_id = data['searchEngineId']

        self.google_api_key = google_api_key
        self.google_cse_id = google_cse_id
"""        