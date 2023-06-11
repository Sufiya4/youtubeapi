from googleapiclient.discovery import build

api_key = 'AIzaSyC2tI41I-8DrcgNEmt_Xmt0-zt1_uI3mZ0'

youtube = build('youtube', 'v3', developerKey=api_key)

#the playlistid is romee strijds
pl_request  = youtube.playlistItems().list(part = 'contentDetails, snippet', playlistId = "PLOm0szp-Cn3SDwHB_6mZ8-4CPIwD2JgEU")

pl_response = pl_request.execute()

#to append video ids of videoa in Playlist to a list
vid_ids=[]
for item in pl_response['items']:
    vid_ids.append(item['contentDetails']['videoId'])
      
vid_request = youtube.videos().list(part = 'snippet, contentDetails, statistics', id = "','.join(vid_ids)")

vid_response = vid_request.execute()
print(vid_response)