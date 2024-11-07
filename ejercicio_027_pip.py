# pip install gTTS
from gtts import gTTS
import os
tts = gTTS('Hola, ¿a que Python es apasionante?', lang='es')
tts.save('hello.mp3')
os.system('start hello.mp3')
