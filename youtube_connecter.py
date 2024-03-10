from googleapiclient.discovery import build
SERVICE_NAME='youtube'
VERSION='v3'
playlist_id='PL-iwWIXCptDxMMTT7MOQBAPoLDeFukrsd'

def get_api_key():
	api_key = open("api_key", "r")
	return api_key.read()

def youtube():
	return build(SERVICE_NAME, VERSION, developerKey=get_api_key())
	
