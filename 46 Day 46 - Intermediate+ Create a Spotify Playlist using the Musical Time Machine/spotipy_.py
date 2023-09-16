import spotipy
import pprint
from spotipy.oauth2 import SpotifyOAuth
import musical_playlist_creator

client_id = '41a2a7c4cbfc40598838afb53126caf5'
client_secret = '16353ab03aba4b28a947536d49e93d83'
redirect_uri = 'http://localhost:3000'
user_id = '21cr6u47cuzxxbjkkq5ltmiti'


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope="playlist-modify-private"))

track_uri = []
for i in musical_playlist_creator.song_titles:
    track_id = sp.search(q='year:' + str(2020) + ' track:' + i, type='track')
    try:
        uri = track_id['tracks']['items'][0]['id']
    except IndexError:
        pprint.pprint(track_id)
        continue
    track_uri.append(uri)


# Create a playlist
    # Create a playlist in your account
    # Name the playlist "YYYY-MM-DD Billboard Top 100"
    # Get the playlist id
my_playlist = sp.user_playlist_create(user=user_id,
                                      name=f'{musical_playlist_creator.year} Billboard Top 100',
                                      public=False,
                                      description=f'What the world loved in {musical_playlist_creator.year}')

my_playlist_id = (my_playlist['id'])


# For every title in the track_uris, add it to the playlist


sp.playlist_add_items(playlist_id=my_playlist_id, items=track_uri)
