from robots.text import Text
from robots.user_input import user_input

class VideoMakerPython:


    def __init__(self):
        

        self.user_input = user_input()
        self.text = Text(self.user_input['searchTerm'],7)

    def start(self):

        
        robots = {
            'userInput': self.user_input,
            'sourceContentOriginal': self.text.content,
            'souceContentSanitized' : self.text.sanitized_content,
            'sentences': self.text.break_into_sentences()
        }
        
        return robots


if __name__ == '__main__':
     video_maker = VideoMakerPython()
     robo = video_maker.start()
     print(robo)