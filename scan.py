import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import docx
from curses import ascii
import pyttsx3  
from googletrans import Translator       

def ocr_core(image):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\khuchana\Documents\Softwares\tesseract.exe'
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(image)  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text
im = Image.open(r"C:\Users\khuchana\Documents\Projects\PythonScan\german.jpg")  
  

result= ocr_core(im)

print(result)
with open('abc.txt',mode ='w') as file:      
      
                 file.write(result) 
                 print(result) 
                   
p = Translator()                       
# translates the text into german language 
k = p.translate(result,dest='hindi')       
print(k) 
engine = pyttsx3.init() 
  
# an audio will be played which speaks the test if pyttsx3 recognizes it 
engine.say(k)                              
engine.runAndWait()