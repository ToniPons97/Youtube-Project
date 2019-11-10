import os
import pickle
import google.oauth2.credentials


from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

CLIENT_SECRETS_FILE = "client_secret.json"
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


def get_authenticated_service():
    credentials = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)
    #  Check if the credentials are invalid or do not exist
    if not credentials or not credentials.valid:
        # Check if the credentials have expired
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_console()
 
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)
 
    return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)


service = get_authenticated_service()

title = []
videoId = []
channelId = []
channelTitle = []
categoryId = []
viewCount = []
favoriteCount = []
likeCount = []
dislikeCount = []
commentCount = []



def search_videos_by_keyword(service, **kwargs):
    results = service.search().list(**kwargs).execute()
    for item in results['items']:
        title.append(item['snippet']['title'])
        videoId.append(item['id']['videoId'])
        stats = service.videos().list(part='statistics, snippet', id=item['id']['videoId']).execute()
        
        channelId.append(stats['items'][0]['snippet']['channelId']) 
        channelTitle.append(stats['items'][0]['snippet']['channelTitle']) 
        categoryId.append(stats['items'][0]['snippet']['categoryId']) 
        favoriteCount.append(stats['items'][0]['statistics']['favoriteCount'])
        viewCount.append(stats['items'][0]['statistics']['viewCount'])

        try:
            likeCount.append(stats['items'][0]['statistics']['likeCount'])
        except:
            print("Video titled {0}, on Channel {1} Likes Count is not available".format(stats['items'][0]['snippet']['title'], stats['items'][0]['snippet']['channelTitle']))
            print(stats['items'][0]['statistics'].keys())
            likeCount.append("Not available")
                
        try:
            dislikeCount.append(stats['items'][0]['statistics']['dislikeCount'])     
        except:
            print("Video titled {0}, on Channel {1} Dislikes Count is not available".format(stats['items'][0]['snippet']['title'], stats['items'][0]['snippet']['channelTitle']))
            print(stats['items'][0]['statistics'].keys())
            dislikeCount.append("Not available")

        if 'commentCount' in stats['items'][0]['statistics'].keys():
            commentCount.append(stats['items'][0]['statistics']['commentCount'])
        else:
            commentCount.append(0)

    youtube_dict = {'channelId': channelId,'channelTitle': channelTitle,
                    'categoryId':categoryId,'title':title,'videoId':videoId,
                    'viewCount':viewCount,'likeCount':likeCount,'dislikeCount':dislikeCount,
                    'commentCount':commentCount,'favoriteCount':favoriteCount}
 
    return youtube_dict


keyword = input('Enter a keyword: ')
search_videos_by_keyword(service, q=keyword, part='id,snippet', eventType='completed', type='video', order='viewCount')



