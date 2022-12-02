import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = "64c88b176a3c4b29a82b16c22c4f6348"
SPOTIPY_CLIENT_SECRET = "cb9ecd3abf134b8ebd4e633b3cef9bf3"
OAUTH_AUTHORIZE_URL= 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL= 'https://accounts.spotify.com/api/token'

ask = input("Which year you would like to travel to? Write your answer in YYYY-MM-DD format:")
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{ask}/")
website = response.text
soup = BeautifulSoup(website, "html.parser")
song_titles = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
list_of_songs = []
for title in song_titles:
    list_of_songs.append(title.getText().split())

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

results = sp.search(q="artist" + "Brian McKnight", type="artist")
items = results['artists']['items']
print(items)
