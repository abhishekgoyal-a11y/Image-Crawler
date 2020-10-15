
#################################################### LIBRARY IMPORTED ###########################################################

import youtube_dl
import pafy
from googleapiclient.discovery import build
import re
from datetime import timedelta

# regular expression

def regex(text,pattern):
	pattern = re.compile(pattern)
	matches = pattern.findall(text)
	return matches

# CONVERTING INTO SECONDS
# REQUIRE (hours,minutes,seconds)

def time_in_seconds(hours,minutes,seconds):

	if hours!=[]:hours = int(hours[0])
	else:hours=0
	if minutes!=[]:minutes = int(minutes[0])
	else:minutes=0
	if seconds!=[]:seconds = int(seconds[0])
	else:seconds=0

	video_seconds = timedelta(
				hours=hours,
				minutes=minutes,
				seconds=seconds
				).total_seconds()
	minutes,seconds = divmod(int(video_seconds),60)
	hours,minutes = divmod(minutes,60)
	return hours,minutes,seconds,video_seconds


#################################################### VIDEO ###########################################################

class Video:

	# EITHER GIVE VIDEO URL OR VIDEO ID

	def __init__(self,video_url=None,video_id=None):
		self.video_url = video_url
		self.video_id = video_id
		
<<<<<<< HEAD
		self.api_key = 'AIzaSyDbfB-C9-R__MFODWNCePbk2Uy1OseulKc'
=======
		self.api_key = API_KEY
>>>>>>> 6b983af29ce1419271f69c5d08179f442193155a

		self.video_url_id()


	def video_url_id(self):
		if self.video_url==None and self.video_id!=None:
			if not isinstance(self.video_id,list):
				self.video_url=[f"https://www.youtube.com/watch?v={self.video_id}"]
			else:
				url = []
				for v_id in self.video_id:
					url.append(f"https://www.youtube.com/watch?v={v_id}")
				self.video_url=url
		elif self.video_url!=None and self.video_id==None:
			if not isinstance(self.video_url,list):
				if "&list=" in self.video_url:
					self.video_url = self.video_url[0:self.video_url.index("&list=")]
					self.video_id = self.video_url[len("https://www.youtube.com/watch?v="):]
				else:
					self.video_id = self.video_url[len("https://www.youtube.com/watch?v="):]
				self.video_url = [self.video_url]
			else:
				url=[]
				for v_url in self.video_url:
					if "&list=" in v_url:
						url.append(v_url[0:v_url.index("&list=")])
					else:
						url.append(v_url)
				self.video_url=url

		elif self.video_url!=None and self.video_id!=None:
			return 

	# VIDEO DOWNLOAD

	def video_download(self):	
		try:
			with youtube_dl.YoutubeDL({}) as ydl:
				ydl.download(self.video_url)
		except:
			return "Error:- Invalid URL or Internet is not Connected!"

	# VIDEO SIZE(IN BYTES)

	def video_size(self):
		video = pafy.new(self.video_url[0]) 
		streams = video.allstreams 

		for j,i in enumerate(streams):
			if "normal:mp4@1280x720" in str(i):
				stream = streams[j]
			elif "normal:mp4@576x360" in str(i):
				stream = streams[j]

		value = stream.get_filesize() 
		return value

	# VIDEO DETAILS
	# 1.video title
	# 2.image url
	# 3.time in seconds
	# 4.total comments,views
	# 5.total likes,dislikes
	# 6.total time(H:M:S)

	def video_details(self):
		youtube = build('youtube','v3',developerKey=self.api_key)
		video_request=youtube.videos().list(
			part='contentDetails,statistics',
			id=self.video_id
		)
		video_response = video_request.execute()

		video_request1=youtube.videos().list(
			part='snippet',
			id=self.video_id
		)
		video_response1 = video_request1.execute()
		try:
			title = video_response1['items'][0]['snippet']['localized']['title']
			image_url = video_response1['items'][0]['snippet']['thumbnails']['high']['url']

			published_at = video_response1['items'][0]['snippet']['publishedAt']

			duration = video_response['items'][0]['contentDetails']['duration']

			hours = regex(duration,f'(\d+)H')
			minutes = regex(duration,f'(\d+)M')
			seconds = regex(duration,f'(\d+)S')

			total_time_in_seconds = time_in_seconds(hours,minutes,seconds)

	 
			commentCount = video_response['items'][0]['statistics']['commentCount']
			dislikeCount = video_response['items'][0]['statistics']['dislikeCount']
			likeCount = video_response['items'][0]['statistics']['likeCount']
			viewCount = video_response['items'][0]['statistics']['viewCount']

			return {
					"title":title,
					"image_url":image_url,
					"time(in seconds)":int(total_time_in_seconds[3]),
					"commentCount":int(commentCount),
					"dislikeCount":int(dislikeCount),
					"likeCount":int(likeCount),
					"viewCount":int(viewCount),
					"time":[total_time_in_seconds[0],total_time_in_seconds[1],total_time_in_seconds[2]],
					'published_at':published_at
				}
		except:pass