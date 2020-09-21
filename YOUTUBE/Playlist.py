from googleapiclient.discovery import build
from pprint import pprint
from Video import Video

class Platlist:
	def __init__(self,playlist_url=None,playlist_id=None):
		self.playlist_url = playlist_url
		self.playlist_id = playlist_id
		self.nextPageToken=None

		self.video_ids = []
		self.video_urls = []

		self.api_key = 'AIzaSyCFs-0PRFSEiRqPqXoorAXoxR8p7e03jvM'
		
		self.total_size = 0

		self.fetching_urls_id()

	def fetching_urls_id(self):
		if self.playlist_url!=None and self.playlist_id==None:
			youtube = build('youtube','v3',developerKey=self.api_key)
			if "/playlist" in self.playlist_url:
				self.playlist_id = self.playlist_url[len('https://www.youtube.com/playlist?list='):]
			elif "/watch" in self.playlist_url:
				self.playlist_id = self.playlist_url[self.playlist_url.index("&list")+6:]

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
					self.video_urls.append(f"https://www.youtube.com/watch?v={item['contentDetails']['videoId']}")

				self.nextPageToken = self.pl_response.get('nextPageToken')

				if not self.nextPageToken:
					break

	def Total_Size(self):
		total_size = 0 
		for video_url in self.video_urls:
			total_size+=Video(video_url=video_url).video_size()
			print(total_size)


p = Platlist(playlist_url="https://www.youtube.com/watch?v=ZzWaow1Rvho&list=PLxt59R_fWVzT9bDxA76AHm3ig0Gg9S3So")
p.Total_Size()

