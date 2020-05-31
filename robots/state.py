import json 


def save_content(content):

    with open('content.json','w') as json_file:
        json_file.write(json.dumps(content))

def load_content():

    with open('content.json', 'r') as json_file:
        content = json.load(json_file)

    return content
