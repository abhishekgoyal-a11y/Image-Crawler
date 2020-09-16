
###########################################################LIBRARY IMPORTED#################################################################

import youtube_dl
import requests

#####################################################DOWNLOAD VIDEO FROM URL################################################################

def url_video_download(video_links): 
	# checking only one video or mulpliple videos

	# if mulpliple videos
	if isinstance(video_links,list):

		# download video one by one
		for video_link in video_links:
			try:
				r = requests.get(video_link, stream = True) 
				with open(f"{input('Enter File Name:- ')}.mp4", 'wb') as f: 
					for chunk in r.iter_content(chunk_size = 1024): 
						if chunk: 
							f.write(chunk)
				print("Successfully Videos Downloaded!")
			except:
				print("Error:- Invalid URL or Internet is not Connected!")

	# only one video
	else:
		try:
			r = requests.get(video_links, stream = True) 
			with open(f"{input('Enter File Name:- ')}.mp4", 'wb') as f: 
				for chunk in r.iter_content(chunk_size = 1024): 
					if chunk: 
						f.write(chunk)
			print("Successfully Videos Downloaded!")
		except:
			print("Error:- Invalid URL or Internet is not Connected!")


#####################################################DOWNLOAD FROM YOTUBE VIDEO URL#########################################################

def youtube_video_download(video_link):
	try:
		if not isinstance(video_link,list):
			with youtube_dl.YoutubeDL({}) as ydl:
				ydl.download([video_link])
			print("Successfully Videos Downloaded!")
		if isinstance(video_link,list):
			with youtube_dl.YoutubeDL({}) as ydl:
				ydl.download(video_link)
			print("Successfully Videos Downloaded!")
	except:
		print("Error:- Invalid URL or Internet is not Connected!")

#######################################################APPENDING URLS#######################################################################

urls = []

def muliple_url():

	global urls
	video_link=input("Enter URL:-")

	if video_link!="q":
		urls.append(video_link)
		muliple_url()

	else:
		pass

#####################################################MAIN FUNCTION##########################################################################

def main():
		video_link =input("For one video press 1 and for multiple videos press 2 and for quit press q:- ")

		if video_link=="1":
			video_link=input("Enter URL:- ")
			if video_link.startswith("https://www.youtube.com"):
				youtube_video_download(video_link)
			else:
				url_video_download(video_link)

		if video_link=="2":
			muliple_url()
			if urls!=[]:
				for url in urls:
					if url.startswith("https://www.youtube.com"):
						youtube_video_download(url)
					else:
						url_video_download(url)

		if video_link=="q":
			print("QUIT")

		if video_link!="2" and video_link!="1"and video_link!="q":
			main()

#####################################################MAIN FUNCTION START####################################################################

if __name__ == "__main__":
	main()
