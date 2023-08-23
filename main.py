from pprint import pprint
import requests
import time

SPOTIFY_ACCESS_TOKEN = 'BQDuVcXXUnksaejRRygvXfO97lIOo5fyIbRe47ihArquKuRkVKb-r1QO_I6zyosTQz78faQ7LmqZ515zLCEYAH-4wjGXTRvme4N7ZN9DTzIk-Kqj6vW0s-1f43O1wovPAFPjm9lsS6CUKg1MIHrCn8OPfOuFCUaDuMzFwlPmR_8Cas8taoxFZVi6sA'
SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'

def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    resp_json = response.json()

    track_id = resp_json['item']['id']
    track_name = resp_json['item']['name']
    artists = resp_json['item']['artists']
    artists_names = ', '.join(
        [artist['name'] for artist in artists]
    )
    link = resp_json['item']['external_urls']['spotify']

    current_track_info = {
        "id": track_id,
        "name": track_name,
        "artists": artists_names,
        "link": link
    }

    return current_track_info



def main():
    while True:
        current_track_info = get_current_track(
            SPOTIFY_ACCESS_TOKEN
        )

        pprint(current_track_info, indent = 4)
        time.sleep(2)


if __name__ == "__main__":
    main()
