import requests
import json

SpotipyClientID = 'cf7d90688aee4aa49539f99f25891bf3'
SpotipyClientSecret = 'ac6fa02651ce4790a074ebd9c0c6aec7'
SpotipyRedirectURL = 'http://127.0.0.1:8888/callback'

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

auth_manager = SpotifyClientCredentials(
    client_id = SpotipyClientID,
    client_secret = SpotipyClientSecret
)
sp = spotipy.Spotify(auth_manager = auth_manager)

results = sp.search(q = 'The Color Violet', type = 'track', limit = 1)

track = results['tracks']['items'][0]

print("The song name is: ", track['name'])
print("The artist's name is: ", track['artists'][0]['name'])
print("Popularity on a scale of 0-100: ", track['popularity'])