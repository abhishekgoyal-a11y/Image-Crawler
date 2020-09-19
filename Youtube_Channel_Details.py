from googleapiclient.discovery import build
import re
import requests
from pprint import pprint
from datetime import timedelta
from Video_Crawler import youtube_video_download,yotube_video_size


api_key = 'AIzaSyCFs-0PRFSEiRqPqXoorAXoxR8p7e03jvM'

youtube = build('youtube','v3',developerKey=api_key)

# Youtube channel detail
class YoutubeChannelDetails:
	def __init__(self,channel_url):
		self.channel_url=channel_url
		self.status = requests.get(channel_url).status_code
		if self.status==200:
			try:
				# Checking the pattern(get username)
				if self.channel_url.startswith("https://www.youtube.com/user/"):
					self.username=self.channel_url[len("https://www.youtube.com/user/"):]
					ch_request = youtube.channels().list(
						part='contentDetails,statistics',
						forUsername=self.username,
						)
					ch_response = ch_request.execute()
					self.Items = ch_response["items"]
					self.channel_id = self.Items[0]['id']
				elif self.channel_url.startswith("https://www.youtube.com/channel/"):
					channel_id = self.channel_url[len("https://www.youtube.com/channel/"):]
					ch_request = youtube.channels().list(
						part='contentDetails,statistics',
						id=channel_id,
						)
					ch_response = ch_request.execute()
					self.Items = ch_response["items"]
			except:
				return 

	# channel details(subscriber,number of videos,total views)
	def ChannelDetails(self):
		if self.status==200:
			try:
				Stats = self.Items[0]['statistics']

				Subscriber = Stats['subscriberCount']
				Videos = Stats['videoCount']
				Views = Stats['viewCount']

				return(Subscriber,Videos,Views)
			except:
				return "Invalid URL!"
		else:
			return "No URL Found!"

	# number of playlist in youtube channel
	def NumberOfPlaylist(self):
		if self.status==200:
			try:
				pl_request = youtube.playlists().list(
					part='contentDetails,snippet',
					channelId=self.channel_id,
					maxResults=50
					)
				pl_response = pl_request.execute()
				return len(pl_response['items'])
			except:
				return "Invalid URL!"
		else:
			return "No URL Found!"


# Playlist Detials(number of videos,total time to complete playlist)
class PlayListDetails:
	def __init__(self,playlist_url):
		self.playlist_url = playlist_url
		self.nextPageToken=None
		self.count=0
		try:self.status = requests.get(self.playlist_url).status_code
		except:return
		self.video_ids=[]
		self.video_links=[]

		self.total_time = 0

		self.hours_pattern = re.compile(f'(\d+)H')
		self.minutes_pattern = re.compile(f'(\d+)M')
		self.seconds_pattern = re.compile(f'(\d+)S')

		try:
			if self.status==200:
				url_pattern = [
				"https://www.youtube.com/playlist?list=",
				"https://www.youtube.com/watch?v="
				]
				if playlist_url.startswith(url_pattern[0]):
					self.playlist_id=playlist_url[len(url_pattern[0]):]
				elif playlist_url.startswith(url_pattern[1]):
					playlist_url=playlist_url[len(url_pattern[1]):]
					self.playlist_id=playlist_url[(playlist_url.index("=")+1):]
				else:
					print("No Playlist Found!")
				while True:
					pl_request = youtube.playlistItems().list(
						part='contentDetails',
						playlistId=self.playlist_id,
						maxResults=50,
						pageToken=self.nextPageToken
						)
					self.pl_response = pl_request.execute()

					for item in self.pl_response['items']:
						self.video_ids.append(item['contentDetails']['videoId'])
					self.nextPageToken = self.pl_response.get('nextPageToken')

					if not self.nextPageToken:
						break
		except:
			return 

	# Tells total number of videos in playlist
	def NumberOfVideos(self):
		if self.status==200:
			try:
				return len(self.video_ids)
			except:
				return "Invalid URL!"
		else:
			return "No URL Found!"
			
	# total time to complete playlist
	def TotalTime(self):
		try:
			if self.video_ids!=[]:
				for video_id in self.video_ids:
					video_request=youtube.videos().list(
							part='contentDetails',
							id=video_id
						)
					video_response = video_request.execute()
					if video_response['items']!=[]:
						time=video_response['items'][0]['contentDetails']['duration']
						hours = self.hours_pattern.findall(time)
						minutes = self.minutes_pattern.findall(time)
						seconds = self.seconds_pattern.findall(time)
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
						self.total_time+=int(video_seconds)
				minutes,seconds = divmod(self.total_time,60)
				hours,minutes = divmod(minutes,60)
				return hours,minutes,seconds
			else:
				return "No Videos Found!"
		except:
			return "Invalid URL!"

	def PlaylistAllVideosLink(self):
		if self.video_ids!=[]:
			for video in self.video_ids:
				self.video_links.append(f"https://www.youtube.com/watch?v={video}")
			return self.video_links
		else:
			return "No Videos Found!"

	# Atrributes:-
		# 1.no_of_videos
		# 2.froms
		# 3.tos
		# 4.list_of_video
	# 1. no_of_videos:-how number of videos you want to downlaod
	# 2. froms:-from which video you want to downlaod
	# 3. tos:-till which video you want to downlaod
	# 4. if you want to downlaod only one specific video from playlist ,pass same value in froms and tos
	# 5. if you want to downlaod only specific number of video ,pass list of number in list_of_video

	# Example
	# In Playlist 4 videos are there(v1,v2,v3,v4)
	# 1. For download all videos ,don't pass any attribute
	# 2. for download 2 videos ,pass 2 in no_of_videos (no_of_videos=2) It will downlaod v1 and v2
	# 3. for downlaod 2 and 3rd video, pass 2 in froms and 3 in tos (froms=2,tos=3), it will downlaod v2 and v3
	# 4. for download all videos from 2nd video, pass 2 in froms (froms=2), it will download v2,v3 and v4.
	# 5. for download v1 and v4 video, pass [1,4] in list_of_video (list_of_video=[1,4]), it will download only v1 and v4
	def DownloadPlaylistVideos(self,**kwargs):
		no_of_videos,froms,tos=None,None,None
		if 'no_of_videos' in kwargs.keys():
			no_of_videos = kwargs['no_of_videos']
		if 'froms' in kwargs.keys():
			froms = kwargs['froms']
		if 'tos' in kwargs.keys():
			tos = kwargs['tos']
		if 'list_of_video' in kwargs.keys():
			list_of_video = kwargs['list_of_video']
		self.PlaylistAllVideosLink()
		if no_of_videos==None and froms==None and tos==None and list_of_video==None:
			youtube_video_download(self.video_links)
		else:
			if no_of_videos!=None and froms==None and tos==None and list_of_video==None:
				if isinstance(no_of_videos,int):
					if no_of_videos == 0:
						print("Invalid Number!")
					elif no_of_videos>len(self.video_links):
						print(f"In this playlist only {len(self.video_links)} videos are there!") 
					else:
						youtube_video_download(self.video_links[0:no_of_videos])
				else:
					print("Enter Number Only!")
			elif froms!=None and no_of_videos==None and tos==None and list_of_video==None:
				if isinstance(froms,int):
					if froms == 0:
						print("Invalid Number!")
					elif froms>len(self.video_links):
						print(f"In this playlist only {len(self.video_links)} videos are there!") 
					else:
						youtube_video_download(self.video_links[froms-1:])
				else:
					print("Enter Number Only!")
			elif froms!=None and no_of_videos==None and tos!=None and list_of_video==None:
				if isinstance(froms,int) and isinstance(tos,int) :
					if froms == 0 or tos==0:
						print("Invalid Number!")
					elif froms>len(self.video_links) or tos>len(self.video_links):
						print(f"In this playlist only {len(self.video_links)} videos are there!") 
					elif froms>tos:
						print("froms can not be greater!")
					else:
						youtube_video_download(self.video_links[froms-1:tos])
				else:
					print("Enter Number Only!")
			elif froms==None and no_of_videos==None and tos==None and list_of_video!=None:
				if isinstance(list_of_video,list):
					if list_of_video!=[]:
						for video in list_of_video:
							if not isinstance(video,int):			
								print("Enter Number Only!")
							elif video==0:
								print("Invalid Number!")
							elif video>len(self.video_links):
								print(f"In this playlist only {len(self.video_links)} videos are there!") 
							else:
								youtube_video_download(self.video_links[video-1])
					else:
						print("list is empty!")
				else:
					print("Pass Number in list")
			else:
				print("No attribute found!")

	# Size of playlist in Bytes
	def PlaylistSize(self):
		video_size=0
		self.PlaylistAllVideosLink()
		for video_link in self.video_links:
			video_size+=yotube_video_size(video_link)
		return video_size

	def PlaylistDetails(self):
		for item in self.pl_response['items']:
			video_id=item['contentDetails']['videoId']

			video_request=youtube.videos().list(
				part='contentDetails,snippet',
				id=video_id
			)
			video_response = video_request.execute()
			url=video_response['items'][0]['snippet']['thumbnails']['high']['url']
			duration=video_response['items'][0]['contentDetails']['duration']
			channelTitle=video_response['items'][0]['snippet']['channelTitle']
			VideoTitle=video_response['items'][0]['snippet']['title']
			yield (url
			,duration
			,channelTitle
			,VideoTitle)
			




y = YoutubeChannelDetails("https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ")
print(y.ChannelDetails())
