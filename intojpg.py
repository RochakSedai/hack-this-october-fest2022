import os
from os import listdir
from PIL import Image
import requests
import shutil
 
# get the path/directory
folder_dir = r"C:\Users\Dell\Downloads\sample"

for images in os.listdir(folder_dir):
    
    filename = images
    
    # splitting the file name after the last '.'
    separator = '.'
    filename = filename.rsplit(separator, 1)[0]
    
    images = Image.open(fr'C:\Users\Dell\Downloads\sample\{images}')

    # conversion of other mode into RGB so that it can be converted into jpg
    images = images.convert('RGB')
    file_name = filename + '.jpg'
    conversion =  images.save(file_name)
    