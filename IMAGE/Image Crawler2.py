
###########################################################LIBRARY IMPORTED#################################################################

from bs4 import *
import requests
import os

###############################################################CREATE FOLDER################################################################

def folder_create(images):
	try:
		folder_name = input("Enter Folder Name:- ")
		# folder creation
		os.mkdir(folder_name)

	# if folder exists with that name, ask another name
	except:
		print("Folder Exist with that name!")
		folder_create()
		
	# image downloading start
	download_images(images,folder_name)


#################################################DOWNLOAD ALL IMAGES FROM THAT URL##########################################################

def download_images(images,folder_name):
	# intitial count is zero
	count = 0

	# print total images found in URL
	print(f"Total {len(images)} Image Found!")

	# checking if images is not zero
	if len(images)!=0:
		for i,image in enumerate(images):
			# In image tag ,we are fetching image URL
			# 1.data-srcset
			# 2.data-src
			# 3.data-fallback-src
			# 4.src
			try:
				# In image tag ,searching for "data-srcset"
				image_link = image["data-srcset"]
			except:
				try:
					# In image tag ,searching for "data-src"
					image_link = image["data-src"]
				except:
					try:
						# In image tag ,searching for "data-fallback-src"
						image_link = image["data-fallback-src"]
					except:
						try:
							# In image tag ,searching for "src"
							image_link = image["src"]
						except:pass

			# After getting image Image URL
			try:
				r = requests.get(image_link).content
				try:
					r= str(r,'utf-8')
				except UnicodeDecodeError:
					# After checking above condition, Image Download start
					with open(f"{folder_name}/images{i+1}.jpg","wb+") as f:
						f.write(r)
					# counting number of image downloaded 
					count+=1
			except:pass

		# There might be possible, that all images not download
		if count==len(images):
			# if all images download
			print("All Images Downloaded!")
			# if all images not download
		else:
			print(f"Total {count} Images Downloaded Out of {len(images)}")

##################################################MAIN FUNCTION START######################################################################

def main(url):
	# Define headers
	HEADER = {
	    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
	}

	# content of URL
	r = requests.get(url,headers=HEADER)
	soup = BeautifulSoup(r.text,'html.parser')

	# find all images in URL
	images = soup.findAll('img')

	# Call folder create function
	folder_create(images)


	
# take url
url=input("Enter URL:- ")

##################################################CALL MAIN FUNCTION######################################################################
main(url)