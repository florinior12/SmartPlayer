$(document).ready(function () {
    $('button#search_button').click(function() {
           $.ajax({
            url: '/search_song',
              data: JSON.stringify({ query : $('#search_query').val()}),
              type: 'POST',
              success: function(response) {
                  $('#my_container').html(response);
              },
              error: function(response) {
                  console.log("Something went wrong! See response below" )
                  console.log(response)
              },
              contentType: 'application/json;charset=UTF-8'
          });
           return false;
        });
    $('#show_songs').click(function() {
           $.ajax({
            url: '/show_all',
            type: 'GET',
            success: function(response) {
                  $('#my_container').html(response);
              }
          });
           return false;
        });
      $('button.like_button').click(function() {
          var button = $(this);

          $.ajax({
              url: '/add_video',
              data: JSON.stringify({ link:player.getVideoData()['video_id'], title:player.getVideoData()['title']}),
              type: 'POST',
              success: function(response) {
                  $("#love_button").attr("src","static/images/liked.png");
              },
              error: function(response) {
                  console.log("Something went wrong! See response below" )
                  console.log(response)
              },
              dataType: "json",
              contentType: 'application/json;charset=UTF-8'

          });
      });

      $('a.index_page').click(function() {
        $.ajax({
          url  : '/popular_songs',
          type : 'GET',
          success: function(response) {
                  $('#my_container').html(response);
              }
        });
        return false;
      });

      
});

