import sys, os
import ffmpeg
import cv2
from gtts import gTTS

result='result.mkv'
imagePath='image.png'
voisedText='text.mp3'

#creating sound using google Text to Speech
def createSound(text):
    tts = gTTS(text)
    tts.save(voisedText)
    return voisedText;

def createVideoByText():
    
        _fileName, _replacedTime, _replacedText = sys.argv[1:]

        print(_fileName, _replacedTime, _replacedText, sep='\n')
        
        tempSoundFileLocation=createSound(_replacedText)
        
        preparedCommand = 'ffmpeg -loop 1 -i {} -i {} -shortest -acodec copy -vcodec mjpeg {}'.format(imagePath,voisedText,result)
        
        print("Current command is \n"+preparedCommand)
        os.system(preparedCommand)
        
        return result
    

if __name__ == '__main__':
    
    createVideoByText()

    
