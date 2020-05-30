from robots.text import Text
from robots.user_input import user_input

class VideoMakerPython:


    def __init__(self):
        

        self.user_input = user_input()
        self.text = Text(self.user_input['searchTerm'])

    def start(self):

        
        robots = {
            'userInput': self.user_input,
            'sourceContentOriginal': self.text.content,
        }
        
        return robots


if __name__ == '__main__':
     video_maker = VideoMakerPython()
     robo = video_maker.start()
     print(robo)