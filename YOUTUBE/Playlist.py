
#################################################### LIBRARY IMPORTED ###########################################################

from googleapiclient.discovery import build
from Video import Video

#################################################### PLAYLIST ###########################################################

class Playlist:

	# EITHER GIVE PLAYLIST URL OR PLAYLIST ID

	def __init__(self,playlist_url=None,playlist_id=None):
		self.playlist_url = playlist_url
		self.playlist_id = playlist_id
		self.nextPageToken=None

		self.video_ids = []
		self.video_urls = []

		self.api_key = 'AIzaSyDbfB-C9-R__MFODWNCePbk2Uy1OseulKc'
		
		self.total_size = 0

		self.fetching_urls_id()

	# FETCHING ALL VIDEOS URLS AND IDS

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
		elif self.playlist_url==None and self.playlist_id!=None:
			youtube = build('youtube','v3',developerKey=self.api_key)
			
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

	# SIZE OF PLAYLIST (IN BYTES)

	def Total_Size(self):
		total_size = 0 
		print(f"Total {len(self.video_urls)} Videos Found!")
		for video_url in self.video_urls:
			total_size+=Video(video_url=video_url).video_size()
		return total_size

	# PLAYLIST DEPTH DETAILS (GIVE VIDEO WISE)
	# 1.total comments, views, dislikes, likes
	# 3.time in seconds
	# 4.image urls
	# 5.title of videos
	# 6.video urls

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
					"video_url":video_url
				}
			)
		return self.playlist_details

	# PLAYLIST DETAILS 
	# 1.total videos
	# 3.time(hours,minutes,seconds)
	# 4.total comments, views
	# 4.total likes, dislikes

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

	# POPULAR VIDEOS OF PLAYLIST

	# FILTER BY
		# 1.views
		# 2.likes

	# pass "videos" arguement for how many number of popular videos you want.

	# Example:-
	# 1.for filtering by views, "Popular_Videos(views)"
	# 	In playlist 4 videos are there
	# 	top 2 videos from playlist "Popular_Videos(views,videos=2)"
	
	# 2.for filtering by likes, "Popular_Videos(likes)"
	# 	In playlist 4 videos are there
	# 	top 2 videos from playlist "Popular_Videos(likes,videos=2)"


	def Popular_Videos(self,**kwargs):
		self.popular_videos = []
		if "views"==kwargs['param']:
			video_views = {}
			for i in self.Playlist_Depth_Detail():
				video_views[i['total_views']]=i

			for i in sorted(video_views.keys()):
				self.popular_videos.append(video_views[i])
			if "videos" in kwargs:
				return self.popular_videos[0:kwargs["videos"]]
			else:
				return self.popular_videos
		elif "likes"==kwargs['param']:
			video_views = {}
			for i in self.Playlist_Depth_Detail():
				video_views[i['total_likes']]=i

			for i in sorted(video_views.keys()):
				self.popular_videos.append(video_views[i])
			if "videos" in kwargs:
				return self.popular_videos[0:kwargs["videos"]]
			else:
				return self.popular_videos

	# Playlist Download

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

	def Playlist_Download(self,no_of_videos=None,froms=None,tos=None,list_of_video=None):
		if no_of_videos==None and froms==None and tos==None and list_of_video==None:
			# Video(video_url=self.video_urls).video_download()
			return self.video_urls

		elif no_of_videos!=None and froms==None and tos==None and list_of_video==None:
			return self.video_urls[0:no_of_videos]

		elif no_of_videos==None and froms!=None and tos!=None and list_of_video==None:
			try:
				if froms>0 and tos>0:
					return self.video_urls[froms-1:tos]
				elif froms<=0:
					return "froms can not be zero or negative!"
				elif tos<=0:
					return "tos can not be zero or negative!"
			except TypeError:
				return "Invalid Arguement!"

		elif no_of_videos==None and froms!=None and tos==None and list_of_video==None:
			try:
				if froms>0:
					return self.video_urls[froms-1:]
				elif froms<=0:
					return "froms can not be zero or negative!"
			except TypeError:
				return "Invalid Arguement!"

		elif no_of_videos==None and froms==None and tos==None and list_of_video!=None:
			video_list = []
			if list_of_video!=[]:
				for video in list_of_video:
					if isinstance(video ,int):
						if 0<video<=len(self.video_urls):
							video_list.append(self.video_urls[video-1])
						else:
							return "Value can not be negative or zero!"
							break
					else:
						return "Invalid List!"
						break
				return video_list
			else:
				return "list of video is empty!"
