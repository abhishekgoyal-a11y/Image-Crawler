###########################################################LIBRARY IMPORTED#################################################################

from bs4 import *
import requests
from PIL import Image
from resizeimage import resizeimage


######################################TAKE WIDTH AND HEIGHT OF IMAGE IF USER WANT TO RESIZE#################################################

def widheig():
    # define global  
    global width,height

    # input of width and height
    try:
        width = int(input("Enter Width in pixels:- "))
        height = int(input("Enter Height in pixels:- "))

    # if user enter invalid input
    except:
        print("Enter number only!")
        widheig()

    return width,height


##########################################################RESIZE THE IMAGE##################################################################

def resize_image(image_name):
    # asking user want to resize the image or not
    resize = input("Do you want to resize the image(yes/no):- ")

    # if user want to resize the image
    if resize=="yes":

        # asking for width and height
        width,height=widheig()
        print("Resizing image, please wait!")

        # resizing the image
        with open(f'{image_name}.jpg', 'r+b') as f:
            with Image.open(f) as image:
                cover = resizeimage.resize_cover(image, [width, height])
                cover.save(f'{image_name}.jpg', image.format)
        print("Image resized!")

    # if not ignore it.
    if resize=="no":pass

    # if user enter invalid command, again function will run
    if resize!="no" and resize!="yes":
        print("invalid command")
        resize_image(image_name)


##########################################################MAIN FUNCTION START###############################################################

def main():
    try:
        # take image url as input ,and get the content of url
        r = requests.get(input("Enter Image Url:- ")).content

        # checking whether image url is present or not
        try:
            r=str(r,'utf-8')
            print("No image Found")

        # if image url is present
        except UnicodeDecodeError:
            # asking for image file name
            image_name = input("Enter image name:- ")
            # image will download
            with open(f"{image_name}.jpg",'wb+') as f:
                f.write(r)
            print("Image is downloaded!")
            # resize function will run
            resize_image(image_name)

    # if url is not correct or internet is not connected
    except Exception as e:print("Url is Not Found! OR",e)

##########################################################CALL MAIN FUNCTION###############################################################

main()
