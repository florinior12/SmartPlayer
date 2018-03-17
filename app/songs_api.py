import requests
import json
import urllib
from app.helpers import process_title
LAST_FM_API = 'http://ws.audioscrobbler.com/'
GET_TOP_TRACKS = '/2.0/?method=chart.gettoptracks&api_key='
SEARCH_TRACK = '/2.0/?method=track.search&track='
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

def search_track(track_name,key):
  track_name = process_title(track_name)
  print(track_name)
  url = LAST_FM_API + SEARCH_TRACK + urllib.parse.quote_plus(track_name) + '&api_key=' + key + FORMAT_JSON
  my_resp = requests.get(url)
  data = json.loads(my_resp.content)
  try:
    tracks = data['results']['trackmatches']['track']
    first_track = tracks[0]
    return {'artist':first_track['artist'], 'title':first_track['name']}
  except Exception as e:
    return {'artist':'Unknown artist', 'title':'Unknown song'}
  

