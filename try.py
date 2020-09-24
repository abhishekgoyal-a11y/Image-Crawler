from googleapiclient.discovery import build
from pprint import pprint


api_key = 'AIzaSyCFs-0PRFSEiRqPqXoorAXoxR8p7e03jvM'

youtube = build('youtube','v3',developerKey=api_key)

pl_request = youtube.playlists().list(
	part='contentDetails',
	channelId="UC4JX40jDee_tINbkjycV4Sg",
	maxResults=50
	)
pl_response = pl_request.execute()
# pprint(pl_response)
print(len(pl_response['items']))