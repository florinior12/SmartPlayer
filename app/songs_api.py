import requests
import json
import urllib
import random
from app.helpers import process_title, process_name
LAST_FM_API = 'http://ws.audioscrobbler.com/2.0/'
GET_TOP_TRACKS = 'chart.gettoptracks'
SEARCH_TRACK = 'track.search'
TRACK_INFO = 'track.getInfo'
TOP_TAGS = 'track.gettoptags'
ARTIST_TOP_TRACKS = 'artist.getTopTracks'
TAG_TOP_TRACKS = 'tag.getTopTracks'
FORMAT_JSON = '&format=json'

def top_tracks(key):
  url = LAST_FM_API + '?method=' + GET_TOP_TRACKS + '&api_key=' +  key + FORMAT_JSON
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
    print('Problem getting top tracks')
    my_resp.raise_for_status() 

  return to_return

def search_track(track_name,key):
  track_name = process_title(track_name)
  #print(track_name)
  url = LAST_FM_API + '?method=' + SEARCH_TRACK + '&track=' + urllib.parse.quote_plus(track_name) + '&api_key=' + key + FORMAT_JSON
  my_resp = requests.get(url)
  data = json.loads(my_resp.content)
  try:
    tracks = data['results']['trackmatches']['track']
    first_track = tracks[0]
    return {'artist':first_track['artist'], 'title':first_track['name']}
  except Exception as e:
    return {'artist':'Unknown artist', 'title':'Unknown song'}
  
def track_info(artist,track, key):

  url = LAST_FM_API + '?method=' + TRACK_INFO + '&api_key=' + key + '&artist=' + artist + '&track=' + track + FORMAT_JSON
  my_resp = requests.get(url)
  data = json.loads(my_resp.content)

def track_tags(artist,track, key):
  artist,track = process_name(artist,track)

  url = LAST_FM_API + '?method=' + TOP_TAGS + '&api_key=' + key + '&artist=' + artist + '&track=' + track + FORMAT_JSON
  my_resp = requests.get(url)
  data = json.loads(my_resp.content)
  with open('cev.json','w+') as f:
    f.write(url)


  tags = ''
  for tag in data['toptags']['tag'][:5]:
    tags += tag['name'] + ";"

  return tags[:-1]  #to remove last semi-colon

def artist_top_tracks(artist,key):
  url = LAST_FM_API + '?method=' + ARTIST_TOP_TRACKS + '&artist=' + urllib.parse.quote_plus(artist) + '&api_key=' + key + FORMAT_JSON
  my_resp = requests.get(url)
  to_return = []

  if(my_resp.ok):
    data = json.loads(my_resp.content)
    tracks = data['toptracks']['track']
    for track in tracks:
      to_return.append({'track_name':track['name'],
              'artist' : artist,
              'thumbnail' : track['image'][1]['#text']
              })
  else:
    print('Problem getting artist ' + artist + ' top tracks')
    my_resp.raise_for_status() 
  return to_return

def genre_top_tracks(artist,track,key):
  limit = 5
  to_return = []
  tags = track_tags(artist,track,key)
  if tags:
    for tag in tags.split(';'):
      page = random.randint(1,100)
      url = LAST_FM_API + '?method=' + TAG_TOP_TRACKS + '&tag=' + urllib.parse.quote_plus(tag) + '&api_key=' + key + '&limit=' + str(limit) + '&page=' + str(page) + FORMAT_JSON
      my_resp = requests.get(url)
      if(my_resp.ok):
        data = json.loads(my_resp.content)
        tracks = data['tracks']['track']
        for track in tracks:
          to_return.append({'track_name':track['name'],
                  'artist' : track['artist']['name'],
                  'thumbnail' : track['image'][1]['#text'],
                  'tag' : tag
                  })
      else:
        print('Problem getting tag ' + tag + 'top tracks')
        my_resp.raise_for_status() 

  return to_return



