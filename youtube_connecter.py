from googleapiclient.discovery import build
SERVICE_NAME='youtube'
VERSION='v3'
API_KEY='AIzaSyBvpL_mFt3n6_i2AtgXVxCLCz7qj3vlzEc'
playlist_id='PL-iwWIXCptDyWB9hg2c_qamBhbAmhFw7d'

def youtube():
	return build(SERVICE_NAME, VERSION, developerKey=API_KEY)