from googleapiclient.discovery import build

api_key = 'AIzaSyC2tI41I-8DrcgNEmt_Xmt0-zt1_uI3mZ0'

youtube = build('youtube', 'v3', developerKey=api_key)

#the channelid is romee strijds
pl_request  = youtube.playlists().list(part = 'contentDetails, snippet', channelId = "UCOXFVINC6GCo86LBy0NQCIg")

response = pl_request.execute()

#to display playlist titles and ids
for item in response['items']:
        print(item['snippet']['title'])
        print(item['id'])
        print()