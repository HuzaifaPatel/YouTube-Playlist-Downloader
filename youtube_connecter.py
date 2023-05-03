from googleapiclient.discovery import build
SERVICE_NAME='youtube'
VERSION='v3'
API_KEY='AIzaSyByaGARKb5XBFPvuc4nl_3B9TfoJDQxkZw'
playlist_id='PL-iwWIXCptDxMMTT7MOQBAPoLDeFukrsd'

def youtube():
	return build(SERVICE_NAME, VERSION, developerKey=API_KEY)
	