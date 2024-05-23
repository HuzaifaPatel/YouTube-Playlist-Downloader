from youtube_connecter import youtube, playlist_id
import os
import yt_dlp as youtube_dl
import logging
PATH = ""
playlist = input("What playlist do you want to download? ")

if playlist == 'stream':
	PATH="/home/huzi/Music/Stream/"
	playlist_id = "PL-iwWIXCptDxMMTT7MOQBAPoLDeFukrsd"
elif playlist == 'chill':
	PATH="/home/huzi/Music/Chill/"
	playlist_id = "PL-iwWIXCptDyWB9hg2c_qamBhbAmhFw7d"


def get_playlist(token_offset):

	return youtube().playlistItems().list (	
															
	part="snippet", 
	id=None, 
	maxResults=50, 
	onBehalfOfContentOwner=None, 
	pageToken=token_offset, 
	playlistId=playlist_id, 
	videoId=None, 
	x__xgafv=None
						
	).execute()


def get_youtube_video_id():
	playlist_data = get_playlist(None)

	while 'nextPageToken' in playlist_data:
		for item in playlist_data['items']:
			download_video_mp3("https://www.youtube.com/watch?v=" + item['snippet']['resourceId']['videoId'], item['snippet']['title'])
		playlist_data = get_playlist(playlist_data['nextPageToken'])


def download_video_mp3(youtube_url, video_name):
	os.chdir(PATH)

	if os.path.exists(video_name + ".mp3") or os.path.isfile(video_name + ".wav"):
		return
	else:
		try:
			ydl_opts = {
				'outtmpl': '%(title)s.%(ext)s',
				'quiet' : True,
				'noplaylist' : True,
				# 'download_archive' : PATH + ".log.txt",
				'format' : 'bestaudio/best',
				'keepvideo': False,
				'postprocessors': [{
		         'key': 'FFmpegExtractAudio',
		         'preferredcodec': 'mp3',
		         'preferredquality': '192',
		     }]
			}

			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				ydl.download([youtube_url])
		except Exception as e:
			logging.warning("Failed Download: " + youtube_url)

get_youtube_video_id()
