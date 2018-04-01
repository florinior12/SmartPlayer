from app.models import Songs
import urllib
def parse_response(response):
  video_list = []

  for video in response[1]:
      _id =  video['id']['videoId']
      _title = video['snippet']['title']
      _date = video['snippet']['publishedAt'].split('T')[0]
      _thumbnail = video['snippet']['thumbnails']['default']['url']
      _liked = search_liked(_id)

      video_list.append({'id':_id,
        'title':_title,
        'date':_date,
        'thumbnail':_thumbnail,
        'liked':_liked
        })

  #print(video_list)
  if len(video_list)>1:
    return video_list
  else:
    return video_list[0]

def search_liked(link):
  if Songs.query.filter_by(song_link=link).first():
    return 'liked'
  else:
    return 'not_liked'

def process_title(title):
  title = title.lower()
  print('Lower title' + title)
  keywords_to_remove = ['official video', 'official audio', 'official music video', 'lyric video', 'audio', 'official lyric video', '[]', '()' ]
  for kw in keywords_to_remove:

    title = title.replace(kw,'')

  return title

def process_name(*args):
  return urllib.parse.quote_plus(args[0].strip().lower()), urllib.parse.quote_plus(args[1].strip().lower())
