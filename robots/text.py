import Algorithmia
import json
import re
import pysbd
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions



class Text:
    

    def __init__(self, search_term: str, maximum_sentences: int):

        self.search_term = search_term
        self.limit_sentences = maximum_sentences
        self.set_algorithmia_api_key()
        self.set_wikipedia_content(search_term)
        self.set_sanitized_content()
        self.set_watson_api_key_and_url()

    def set_algorithmia_api_key(self):

        with open('credentials/algorithmia.json', 'r') as json_file:
            data = json.load(json_file)
            api_key = data['apiKey'] 

        self.algorithmia_api_key = api_key

    def set_watson_api_key_and_url(self):

        with open('credentials/watson-nlu.json', 'r') as json_file:
            data = json.load(json_file)
            api_key = data['apikey'] 
            url = data['url']

        self.watson_api_key, self.watson_url = api_key, url

    def set_wikipedia_content(self, search_term):

        input = {
        "articleName": self.search_term,
        "lang": "en"
        }

        algorithmia_autenticated = Algorithmia.client(self.algorithmia_api_key)
        wikipedia_algorithm = algorithmia_autenticated.algo('web/WikipediaParser/0.1.2')
        wikipedia_algorithm.set_options(timeout=300) # optional
        wikipedia_content = wikipedia_algorithm.pipe(input).result
        
        self.content = wikipedia_content['content']

    @staticmethod
    def treat_text(text):
            
        all_lines = text.split('\n')
        without_blank_lines = list(filter(lambda phrase: phrase != '', all_lines))
        without_blank_lines_and_markdown = list(filter(lambda phrase: not phrase.startswith('='), without_blank_lines))
        text = ' '.join(without_blank_lines_and_markdown)

        return re.sub('\(.*?\)', '',text)

    def set_sanitized_content(self):
        self.sanitized_content = self.treat_text(self.content)

    def fetch_keywords_sentences(self, sentence):

        authenticator = IAMAuthenticator(self.watson_api_key)
        natural_language_understanding = NaturalLanguageUnderstandingV1(
            version='2020-05-31',
            authenticator=authenticator)

        natural_language_understanding.set_service_url(self.watson_url)

        response = natural_language_understanding.analyze(
            text= sentence,
            features=Features(
                keywords=KeywordsOptions())).get_result()

        keywords = []

        for keyword in response['keywords']:
            keywords.append(keyword['text'])

        return keywords

    def break_into_sentences(self):

        text = self.sanitized_content
        seg = pysbd.Segmenter(language="en", clean=False)
        
        sentences = []
        for sentence in seg.segment(text)[0:self.limit_sentences]:
            content = {
                "text":sentence,
                "keywords": self.fetch_keywords_sentences(sentence),
                "images":[]
            }
            sentences.append(content)

        return sentences
    
            
            

if __name__=='__main__':
    content = Text('Michael Jackson')

    print(content.break_into_sentences())


