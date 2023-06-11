from googleapiclient.discovery import build
import re
from datetime import timedelta
 
api_key = 'AIzaSyC2tI41I-8DrcgNEmt_Xmt0-zt1_uI3mZ0'

youtube = build('youtube', 'v3', developerKey=api_key)

#the playlistid is romee strijds workout
pl_request  = youtube.playlistItems().list(part = 'contentDetails, snippet', playlistId = "PLOm0szp-Cn3QmaHc3MvHLdVWr6jCpVzUi")
pl_response = pl_request.execute()

#to append video ids of video in Playlist to a list
vid_ids=[]
for item in pl_response['items']:
    vid_ids.append(item['contentDetails']['videoId'])
      
vid_request = youtube.videos().list(part = 'snippet, contentDetails, statistics', id = vid_ids)
vid_response = vid_request.execute()

totalseconds = 0

print("these are the hours,mins,seconds")
for item in vid_response['items']:
    duration = item['contentDetails']['duration']
    
    hours = re.compile(r'(\d+)H').search(duration)
    hours = int(hours.group(1)) if hours else 0

    minutes = re.compile(r'(\d+)M').search(duration)
    minutes = minutes.group(1) if minutes else 0

    seconds = re.compile(r'(\d+)S').search(duration)
    seconds = seconds.group(1) if seconds else 0

    print(hours, minutes, seconds)
    print()
    vid_seconds = timedelta(hours=int(hours), minutes=int(minutes),seconds=int(seconds)).total_seconds()
    totalseconds += vid_seconds

print("totalseconds:")
print(totalseconds)
totalseconds = int(totalseconds)
minutes, seconds = divmod(totalseconds, 60)
hours, minutes = divmod(minutes, 60)
print("total duration of playlist:")
print(hours, minutes, seconds)