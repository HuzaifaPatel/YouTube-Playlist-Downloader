from googleapiclient.discovery import build
SERVICE_NAME='youtube'
VERSION='v3'
playlist_id='PL-iwWIXCptDxMMTT7MOQBAPoLDeFukrsd'

def get_api_key():
	api_key_file = open("api_key", "r")
	api_key = api_key_file.read()
	api_key_file.close()
	return api_key
API_KEY = get_api_key()

def youtube():
	return build(SERVICE_NAME, VERSION, developerKey=API_KEY)
	
