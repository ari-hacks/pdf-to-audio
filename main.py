from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pdftotext
from gtts import gTTS
import os 

"""
Tkinter works with pipenv shell
"""
Tk().withdraw() 
filelocation = askopenfilename() 
print(filelocation)

"""
TODO: With docker using file path instead of tkinter, get this to work with GUI
"""
# fileDir = os.path.dirname(os.path.realpath('__file__'))
# file_path = os.path.join(fileDir, 'input2.pdf')
# print(fileDir)
# print(file_path)

with open(filelocation, "rb") as f:  
    #pdf = open(file_path)
    pdf = pdftotext.PDF(f)  

string_of_text = ''
for text in pdf:
    string_of_text += text
    print(string_of_text)

final_file = gTTS(text=string_of_text, lang='en')  
final_file.save(file_path +".mp3")  
print('finished saving to audio file')