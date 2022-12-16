
from inspect import trace
import spotipy
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time 
from datetime import timedelta

auth_manager = SpotifyClientCredentials(client_id= 'clientid',
client_secret='clientsecret')

sp = spotipy.Spotify(auth_manager=auth_manager)

def getTrackIDs(user ,playlist_id):
    track_ids=[]
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist ['tracks']['items']:
        track = item[ 'track']
        track_ids.append(track['id'])
    return track_ids
track_ids = getTrackIDs ('spotify','Spotify Uri')


def getTrackFeatures(id):
    track_info = sp.track(id)
    features_info = sp.audio_features(id)
    name = track_info['name']
    artist = track_info['album']['artists'][0]['name']
    length = track_info['duration_ms']
    length_m = timedelta(milliseconds=length)
    track_data = [artist,name, length_m]
    return track_data



track_list = []
num_tracks = len(track_ids)
for i in range(len(track_ids)):
    #time.sleep(1)

    track_data = getTrackFeatures(track_ids[i])
    track_list.append(track_data)
    print(num_tracks, 'songs left')
    num_tracks -= 1





dj_playlist = pd.DataFrame(track_list , columns=[ 'Artist','Name', 'Duration'])
dj_playlist.head(10)
print(dj_playlist)
