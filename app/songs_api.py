import requests
import json

LAST_FM_API = 'http://ws.audioscrobbler.com/'
GET_TOP_TRACKS = '/2.0/?method=chart.gettoptracks&api_key='
FORMAT_JSON = '&format=json'

def top_tracks(key):
  url = LAST_FM_API + GET_TOP_TRACKS + key + FORMAT_JSON
  my_resp = requests.get(url)
  to_return = []

  if(my_resp.ok):
    data = json.loads(my_resp.content)
    tracks = data['tracks']['track']
    for track in tracks:
      to_return.append({'track_name':track['name'],
              'artist' : track['artist']['name'],
              'thumbnail' : track['image'][1]['#text']
              })
  else:
     my_resp.raise_for_status() 

  return to_return
