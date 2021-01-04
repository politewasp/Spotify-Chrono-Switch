import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from credentials import *
import util


def main():
    client_credentials_manager = SpotifyClientCredentials(client_id=os.environ['USER'],
                                                          client_secret=os.environ['PASS'])
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    playlists = sp.user_playlists('mi.matson42')
    get_uri_by_name = {}
    get_playlist_by_index = []

    while playlists:
        for i, playlist in enumerate(playlists['items']):
            get_uri_by_name[playlist['name']] = playlist['uri']
            get_playlist_by_index.append({'name': playlist['name'], 'uri': playlist['uri']})
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None

    intense_work_playlist_name = 'radar systems make me want to fucking die'
    intense_work_playlist_uri = get_uri_by_name[intense_work_playlist_name]

    casual_work_playlist = util.pick_playlist(get_playlist_by_index, casual_work_mask)
    casual_work_playlist_name = casual_work_playlist['name']
    casual_work_playlist_uri = casual_work_playlist['uri']

    new_pollution = 'spotify:track:4t5tAOTFUfb2FhHnnapWlB'
    politewasp_auth_token = 'BQC6V81yGKQmlo1aQkqar11znMjKaBgnkARIic34YdEm6v0nIO0DLXOaahEaNOnC8d_toPg8e-oy8zeHhwlKJf8hxNFlletpyEYqDi479cLtYy9FXej0gwT6nD0Ar5lc6ku9xeBk0Z_LfLtg0YUDibakE47YzJyDktgb0vCTsLWLBTn8r-FVriw8kZC4c7N3GVb-dsGj5ObruPGt1czGUsEgBplt9bQSL0qWenwbYG1QCFKtc4X4RWsRa8wkGIGJM3nFlDG0_GKdejI-ZxJQ'
    user = sp.user('mi.matson42')

    client = spotipy.client.Spotify(auth=politewasp_auth_token)

    print(user)
    # client.add_to_queue(uri=new_pollution)


if __name__ == '__main__':
    main()
