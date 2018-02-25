def parse_response(response):
  video_list = []
  for video in response[1]:
      _id = video['id']['videoId']
      _title = video['snippet']['title']
      _date = video['snippet']['publishedAt'].split('T')[0]
      _thumbnail = video['snippet']['thumbnails']['default']['url']
      video_list.append({'id':_id,
        'title':_title,
        'date':_date,
        'thumbnail':_thumbnail})

  print("Parsed a total of " + str(len(video_list)) + " videos")
  #print(video_list)
  return video_list
