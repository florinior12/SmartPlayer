from app.models import Songs
import urllib
#this method is used to parse the response of the youtube search API
def parse_response(response):
  #video_list is a list containing all the videos received when searching for a song on youtube
  video_list = []
  #each video is an element in a json array
  for video in response[1]:
      _id =  video['id']['videoId']
      _title = video['snippet']['title']
      _date = video['snippet']['publishedAt'].split('T')[0]
      _thumbnail = video['snippet']['thumbnails']['default']['url']
      _liked = search_liked(_id)

      #add the song (as a dictionary) to the list 
      video_list.append({'id':_id,
        'title':_title,
        'date':_date,
        'thumbnail':_thumbnail,
        'liked':_liked
        })

  #when the result is just one video, we return only one, as an element
  if len(video_list)>1:
    return video_list
  else:
    return video_list[0]

#this method looks for a certain song in the database by the link, if it's found then the song is liked
def search_liked(link):
  if Songs.query.filter_by(song_link=link).first():
    return 'liked'
  else:
    return 'not_liked'

#this method removes unnecesary words from youtube video titles in order to be able to search for the song on last fm api
def process_title(title):
  title = title.lower()
  #print('Lower title' + title)
  keywords_to_remove = ['official video', 'official audio', 'official music video', 'lyric video', 'audio', 'official lyric video', '[]', '()' ]
  for kw in keywords_to_remove:

    title = title.replace(kw,'')

  return title


def process_name(*args):
  return urllib.parse.quote_plus(args[0].strip().lower()), urllib.parse.quote_plus(args[1].strip().lower())
