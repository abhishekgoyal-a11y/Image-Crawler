
#################################################### LIBRARY IMPORTED ###########################################################

from googleapiclient.discovery import build
from Video import Video
from Playlist import Playlist

#################################################### CHANNEL ###########################################################

class Channel:

	# EITHER GIVE CHANNEL USERNAME OR ID OR URL

	def __init__(self,channel_username=None,channel_id=None,channel_url=None):
		self.channel_username = channel_username
		self.channel_id = channel_id
		self.channel_url = channel_url

		self.api_key = 'AIzaSyCFs-0PRFSEiRqPqXoorAXoxR8p7e03jvM'

		self.channel_url_id_username()

	# FETCHING ALL VIDEO URLS, USERNAME AND ID 

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

	# COUNT NUMBER OF PLAYLIST
	# REQUIRE ONLY CHANNEL ID

	def no_of_playlist(self,channel_id=None):
		return len(self.Channel_Depth_details(channel_id))

	# CHANNEL DETAILS INCLUDE
	# 1.total subscribers
	# 2.total videos
	# 3.total views

	# For more details set depth to be True
	# it includes, playlists images,url,title
	
	def Channel_details(self,depth=None):
		if self.channel_id!=None and self.channel_username==None:
			if depth==None or depth==False:
				total_subscriber = self.ch_response['items'][0]['statistics']['subscriberCount']
				total_videos = self.ch_response['items'][0]['statistics']['videoCount']
				total_views = self.ch_response['items'][0]['statistics']['viewCount']
				number_of_playlist = self.no_of_playlist(channel_id=self.channel_id)
				return (total_subscriber,total_views,total_videos,number_of_playlist)

			elif depth==True:
				return self.Channel_Depth_details(self.channel_id)


		elif self.channel_id==None and self.channel_username!=None:
			if "items" in self.ch_response:
				channel_id = self.ch_response['items'][0]['id']
				if depth==None or depth==False:
					total_subscriber = self.ch_response['items'][0]['statistics']['subscriberCount']
					total_videos = self.ch_response['items'][0]['statistics']['videoCount']
					total_views = self.ch_response['items'][0]['statistics']['viewCount']
		
					number_of_playlist = self.no_of_playlist(channel_id=channel_id)
					return (total_subscriber,total_views,total_videos,number_of_playlist)

				elif depth==True:
					return self.Channel_Depth_details(channel_id)

			else:
				return "No Playlist Found!"

	# CHANNEL DEPTH DETAILS
	# REQUIRE ONLY CHANNEL ID

	def Channel_Depth_details(self,channel_id):
		pl_request = self.youtube.playlists().list(
					part='contentDetails,snippet',
					channelId=channel_id,
					maxResults=50
					)
		pl_response = pl_request.execute()

		details = []

		for r in pl_response['items']:
			details.append(
					(
						r['snippet']['localized']['title'],
						r['snippet']['thumbnails']['high']['url'],
						"https://www.youtube.com/playlist?list="+str(r['id'])

					)
				)
		return details
		