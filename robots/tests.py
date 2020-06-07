from wand.image import Image
from state import load_content
import subprocess

content = load_content()['sentences']
total_sentences = len(content)

def resize_images():
    
    for index in range(0, total_sentences):
        command = f"magick content/{index}original.jpg\
            -resize 1920x1080 \
            content/{index}original.jpg"

        subprocess.run(command, shell=True)

def compose_images():
    
    for index in range(0,total_sentences):
        with Image(filename=f'content/{index}original.jpg') as img:
            with img.clone() as background:
                background.resize(1920,1080)
                background.blur(radius=0, sigma=10)

                with Image(width=background.width, height=background.height) as imgcompose:
                    #img.resize(int(img.width*1.5),int(img.height*1.5))
                    imgcompose.composite(image=background, left=0,top=0)
                    imgcompose.composite(image=img,operator='over', gravity='center')
                    imgcompose.save(filename=f'content/{index}converted.jpg')
        
def create_sentence_image(sentence, sentence_index):

    sentence = sentence
    sentence_index = sentence_index
    template_settings = {
        0: {
          'size': '1920x400',
          'gravity': 'center'
        },
        1: {
          'size': '1920x1080',
          'gravity': 'center'
        },
        2: {
          'size': '800x1080',
          'gravity': 'west'
        },
        3: {
          'size': '1920x400',
          'gravity': 'center'
        },
        4: {
          'size': '1920x1080',
          'gravity': 'center'
        },
        5: {
          'size': '800x1080',
          'gravity': 'west'
        },
        6: {
          'size': '1920x400',
          'gravity': 'center'
        }

      }

    size = template_settings[sentence_index]['size']
    gravity =  template_settings[sentence_index]['gravity']

    command =f'magick -size {size} \
    -background transparent\
    -gravity {gravity} \
    -pointsize 50\
    -fill white \
    -kerning -1 \
    caption:"{sentence}"\
    content/{sentence_index}sentence.png'
    try:
        subprocess.run(command, shell=True)
    except:
        print('Something went wrong while running the command line')

def start_robot():
    resize_images()
    compose_images()
    
    for index in range(0,total_sentences):
        create_sentence_image(content[index]['text'], index)

if __name__=='__main__':
    start_robot()