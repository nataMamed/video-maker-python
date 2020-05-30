import Algorithmia
import json
import re
import pysbd



class Text:
    

    def __init__(self, search_term: str):

        self.search_term = search_term
        self.set_api_key()
        self.set_wikipedia_content(search_term)
        self.set_sanitized_content()

    def api_key(self):
        return self.api_key

    def set_api_key(self):

        with open('credentials/algorithmia.json', 'r') as json_file:
            data = json.load(json_file)
            apikey = data['apiKey'] 

        self.api_key = apikey

    def set_wikipedia_content(self, search_term):

        input = {
        "articleName": self.search_term,
        "lang": "en"
        }

        algorithmia_autenticated = Algorithmia.client(self.api_key)
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

    def break_into_sentences(self):

        text = self.sanitized_content
        seg = pysbd.Segmenter(language="en", clean=False)

        sentences = []
        for sentence in seg.segment(text):
            content = {
                'text':sentence,
                'keywords':[],
                'images':[]
            }
            sentences.append(content)
        return sentences
    
            
            

if __name__=='__main__':
    content = Text('Microsoft')

    print(content.break_into_sentences())


