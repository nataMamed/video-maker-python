from robots.text import Text
from robots.image import Image
from robots.user_input import user_input
from robots.state import save_content, load_content

def start():
    user_input()
    Text().start_robot()
    Image().start_robot()
    #Video().start_Robot()
    #Youtube().start_robot()

if __name__=='__main__':
    start()