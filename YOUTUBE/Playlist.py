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
		print(f"Total {len(self.video_urls)} Videos Found!")
		for video_url in self.video_urls:
			total_size+=Video(video_url=video_url).video_size()
		return total_size

	def Playlist_Depth_Detail(self):

		self.playlist_details=[]

		for video_url in self.video_urls:
			video_details = Video(video_url).video_details()
			self.playlist_details.append(
				{
					"total_comments":video_details['commentCount'],
					"total_dislikes":video_details['dislikeCount'],
					"total_likes":video_details['likeCount'],
					"total_views":video_details['viewCount'],
					"time(in seconds)":video_details['time(in seconds)'],
					"image_url":video_details['image_url'],
					"title":video_details['title'],
				}
			)
		return self.playlist_details

	def Playlist_Details(self):

		self.time_in_second = 0
		self.total_views = 0
		self.total_likes = 0
		self.total_dislikes = 0
		self.total_comments = 0

		for video_url in self.video_urls:
			video_details = Video(video_url).video_details()
			self.total_comments+=video_details['commentCount']
			self.total_dislikes+=video_details['dislikeCount']
			self.total_likes+=video_details['likeCount']
			self.total_views+=video_details['viewCount']
			self.time_in_second+=video_details['time(in seconds)']


		minutes,seconds = divmod(int(self.time_in_second),60)
		hours,minutes = divmod(minutes,60)

		return{
			"Total Videos":len(self.video_urls),
			"Total Hours":hours,
			"Total Minutes":minutes,
			"Total Seconds":seconds,
			"Total Comments":self.total_comments,
			"Total Dislikes":self.total_dislikes,
			"Total Likes":self.total_likes,
			"Total Views":self.total_views
			}


p = Platlist(playlist_url="https://www.youtube.com/watch?v=Wo5dMEP_BbI&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3")
pprint(p.Playlist_Details())

