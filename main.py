# from tkinter import Tk
# from tkinter.filedialog import askopenfilename
# import pdftotext
from gtts import gTTS
import os 

# Tk().withdraw() 
# filelocation = askopenfilename() 
# print(filelocation)

fileDir = os.path.dirname(os.path.realpath('__file__'))
file_path = os.path.join(fileDir, 'input.pdf')
print(fileDir)
print(file_path)

with open(file_path, "rb") as f:  
    pdf = open(file_path)
    #pdf = pdftotext.PDF(f)  

string_of_text = ''
for text in pdf:
    string_of_text += text

final_file = gTTS(text=string_of_text, lang='en')  
final_file.save(file_path +".mp3")  