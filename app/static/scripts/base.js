$(document).ready(function () {
          var liked = false;
          $(function() {
            $('button#like_button').click(function() {
                var video_date = $(this).closest('tr')
                  .prev()
                  .find('td.video_date')
                  .html();
                var video_id = $(this).closest('tr')
                  .prev()
                  .prev()
                  .find('td.video_id')
                  .find('a')
                  .attr('href');
                var video_title = $(this).closest('tr')
                  .prev()
                  .prev()
                  .find('td.video_id')
                  .find('.video_title')
                  .html();
                var button = $(this);
                

                $.ajax({
                    url: '/add_video',
                    data: JSON.stringify({date: video_date, link:video_id, title:video_title}),
                    type: 'POST',
                    success: function(response) {
                        var cell = button.closest('td');
                        if(cell.children('i').length==0) {
                          cell.append('<i> Added song!</i>');
                        }
                    },
                    error: function(response) {
                        console.log("Something went wrong! See response below" )
                        console.log(response)
                    },
                    dataType: "json",
                    contentType: 'application/json;charset=UTF-8'

                });
            });
            $('a#play_id').click(function() {
              player.loadVideoById($(this).attr('href'));
              return false;
            });
            $('a#play_track_name').click(function() {
              var track_name = $(this).text();
              var artist_name = $(this).closest('tr').next().text();
              $.ajax ({
                url : '/play_song',
                data: JSON.stringify({track: track_name, artist: artist_name}),
                type: 'POST',
                success: function(response) {
                  player.loadVideoById(response['id']);

                },
                dataType: "json",
                contentType: 'application/json;charset=UTF-8'
              });
              return  false;
            });
          });


});
