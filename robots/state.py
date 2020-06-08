import json 


def save_content(content):

    with open('content.json','w') as json_file:
        json_file.write(json.dumps(content))

def save_script():
    with open('content/after-effects-script.js', 'w', encoding='utf-8') as file:
        content = load_content()
        content = f'var content = {content}' 
        file.write(content)

def load_content():

    with open('content.json', 'r') as json_file:
        content = json.load(json_file)

    return content
if __name__=='__main__':
    save_script()