from bs4 import *
import requests
from PIL import Image
from resizeimage import resizeimage


def widheig():
    global width,height
    try:
        width = int(input("Enter Width in pixels:- "))
        height = int(input("Enter Height in pixels:- "))
    except:
        print("Enter number only!")
        widheig()
    return width,height



def resize_image(image_name):
    resize = input("Do you want to resize the image(yes/no):- ")
    if resize=="yes":
        width,height=widheig()
        print("Resizing image, please wait!")
        with open(f'{image_name}.jpg', 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_cover(image, [width, height])
                cover.save(f'{image_name}.jpg', image.format)
        print("Image resized!")
    if resize=="no":pass
    if resize!="no" and resize!="yes":
        print("invalid command")
        resize_image(image_name)

try:
    r = requests.get(input("Enter Image Url:- ")).content
    try:
        r=str(r,'utf-8')
        print("No image Found")
    except UnicodeDecodeError:
        image_name = input("Enter image name:- ")
        with open(f"{image_name}.jpg",'wb+') as f:
            f.write(r)
        print("Image is downloaded!")
        resize_image(image_name)
except Exception as e:print("Url is Not Found! OR",e)
