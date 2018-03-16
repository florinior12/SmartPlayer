from app.models import Songs
def parse_response(response):
  video_list = []
  print(response[1])
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

  print("Parsed a total of " + str(len(video_list)) + " videos")
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
