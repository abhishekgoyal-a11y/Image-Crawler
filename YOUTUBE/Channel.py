from googleapiclient.discovery import build
from pprint import pprint
from Video import Video
from Playlist import Playlist

class Channel:
	def __init__(self,channel_username=None,channel_id=None,channel_url=None):
		self.channel_username = channel_username
		self.channel_id = channel_id
		self.channel_url = channel_url

		self.api_key = 'AIzaSyCFs-0PRFSEiRqPqXoorAXoxR8p7e03jvM'

		self.channel_url_id_username()

	def channel_url_id_username(self):

		self.youtube = build('youtube','v3',developerKey=self.api_key)
		if self.channel_url!=None and self.channel_username==None and self.channel_id==None:

			if "channel" in self.channel_url:
				self.channel_id = self.channel_url[len("https://www.youtube.com/channel/"):]
				self.ch_request = self.youtube.channels().list(
					part='statistics',
					id=self.channel_id
					)
			elif "user" in self.channel_url:
				self.channel_username = self.channel_url[len("https://www.youtube.com/user/"):]
				self.ch_request = self.youtube.channels().list(
					part='statistics',
					forUsername=self.channel_username
					)

		elif self.channel_url==None and self.channel_username==None and self.channel_id!=None:
			self.ch_request = self.youtube.channels().list(
					part='statistics',
					id=self.channel_id
					)


		elif self.channel_url==None and self.channel_username!=None and self.channel_id==None:
			self.ch_request = self.youtube.channels().list(
					part='statistics',
					forUsername=self.channel_username
					)

		self.ch_response = self.ch_request.execute()

	def no_of_playlist(self,channel_id=None):
		pl_request = self.youtube.playlists().list(
					part='contentDetails,snippet',
					channelId=channel_id,
					maxResults=50
					)
		pl_response = pl_request.execute()
		return len(pl_response['items'])

	def Channel_details(self):
		if self.channel_id!=None and self.channel_username==None:
			total_subscriber = self.ch_response['items'][0]['statistics']['subscriberCount']
			total_videos = self.ch_response['items'][0]['statistics']['videoCount']
			total_views = self.ch_response['items'][0]['statistics']['viewCount']
			number_of_playlist = self.no_of_playlist(channel_id=self.channel_id)

			return (total_subscriber,total_views,total_videos,'s',number_of_playlist)

		elif self.channel_id==None and self.channel_username!=None:
			if "items" in self.ch_response:
				total_subscriber = self.ch_response['items'][0]['statistics']['subscriberCount']
				total_videos = self.ch_response['items'][0]['statistics']['videoCount']
				total_views = self.ch_response['items'][0]['statistics']['viewCount']
				channel_id = self.ch_response['items'][0]['id']

				number_of_playlist = self.no_of_playlist(channel_id=channel_id)
				return (total_subscriber,total_views,total_videos,number_of_playlist)
			else:
				return "No Playlist Found!"






c = Channel(channel_username="schafer5")

print(c.Channel_details())


channel_url = "https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ"

channel_id = "UCICWIYEx2mo4wYZzLwJ7wVw"

channel_url = "https://www.youtube.com/user/sentdex"

channel_username = "sentdex"