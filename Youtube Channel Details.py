from googleapiclient.discovery import build
import re
import requests
from pprint import pprint
from datetime import timedelta

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
				pattern = re.compile(r'https://www.youtube.com/user/\w+')
				matches = pattern.findall(self.channel_url)
				self.username=matches[0][29:]

				ch_request = youtube.channels().list(
					part='contentDetails,statistics',
					forUsername=self.username,
					)

				ch_response = ch_request.execute()
				self.Items = ch_response["items"]
				self.channel_id = self.Items[0]['id']
			except:
				return "Invalid URL!"

	# channel details(subscriber,total views,number of videos)
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
					print("No URL Found!")
				while True:
					pl_request = youtube.playlistItems().list(
						part='contentDetails',
						playlistId=self.playlist_id,
						maxResults=50,
						pageToken=self.nextPageToken
						)
					pl_response = pl_request.execute()

					for item in pl_response['items']:
						self.video_ids.append(item['contentDetails']['videoId'])
					self.nextPageToken = pl_response.get('nextPageToken')

					if not self.nextPageToken:
						break
		except:
			return 

	# number of videos in playlist
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

