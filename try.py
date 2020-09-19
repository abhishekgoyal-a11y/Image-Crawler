from googleapiclient.discovery import build
from pprint import pprint
import requests
api_key = 'AIzaSyCFs-0PRFSEiRqPqXoorAXoxR8p7e03jvM'

youtube = build('youtube','v3',developerKey=api_key)


pl_request = youtube.playlistItems().list(
	part='contentDetails',
	playlistId="PLWKjhJtqVAbmqFs83T4W-FZQ9kK983tZC",
	maxResults=50
	)
pl_response = pl_request.execute()

for item in pl_response['items']:
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
	print(url)
	print(duration)
	print(channelTitle)
	print(VideoTitle)
	print()