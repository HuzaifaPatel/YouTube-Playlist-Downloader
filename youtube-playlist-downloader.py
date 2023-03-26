from youtube_connecter import youtube, playlist_id

def get_playlist(token_offset):

	return youtube().playlistItems().list (	
															
																part="snippet", 
																id=None, 
																maxResults=1, 
																onBehalfOfContentOwner=None, 
																pageToken=token_offset, 
																playlistId=playlist_id, 
																videoId=None, 
																x__xgafv=None
															
															).execute()


def get_youtube_video_id():
	playlist_data = get_playlist(None)

	while 'nextPageToken' in playlist_data:
		print("https://www.youtube.com/watch?v=" + playlist_data['items'][0]['snippet']['resourceId']['videoId'])
		playlist_data = get_playlist(playlist_data['nextPageToken'])

get_youtube_video_id()