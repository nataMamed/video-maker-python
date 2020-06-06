from wand.image import Image, GRAVITY_TYPES
from wand.display import display

def run_cmd():
    with Image(filename='content/SupermanActionComics.jpg') as img:
        with img.clone() as background:
            background.resize(1920,1080)
            background.blur(radius=0, sigma=10)

            with Image(width=background.width, height=background.height) as imgcompose:
                #img.resize(int(img.width*1.5),int(img.height*1.5))
                imgcompose.composite(image=background, left=0,top=0)
                imgcompose.composite(image=img, left=int((background.width/2)-(img.width/2)), top=int((background.height/2)-(img.height/2)))
                display(imgcompose)
    

if __name__=='__main__':
    run_cmd()

    MAGICK_HOME = 'C:\Program Files\ImageMagick-7.0.10-Q16'