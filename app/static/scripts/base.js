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
    $('input#search_query').on('keydown', function(e) {
        if (e.which == 13) {
            e.preventDefault();
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
        }
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
            data: JSON.stringify({ link:player.getVideoData()['video_id'],
             yt_title:player.getVideoData()['title'],
              artist:$('#song_artist').text(),
               track:$('#song_title').text()}),
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
        type : 'POST',
        data: JSON.stringify({type:'popular'}),
        success: function(response) {
                $('#my_container').html(response);
            },
        contentType: 'application/json;charset=UTF-8'
      });
      return false;
    });    
    $('a.more_artist').click(function() {
      $.ajax({
        url : '/popular_songs',
        type: 'POST',
        data: JSON.stringify({type:'artist_top',artist_name:$('h6#song_artist').text()}),
        success: function(response) {
          $('#my_container').html(response);
        },
        contentType: 'application/json;charset=UTF-8'
      });
      return false;
    });
    $('a.more_genre').click(function() {
      $.ajax({
        url : '/popular_songs',
        type: 'POST',
        data: JSON.stringify({type:'genre_top',artist_name:$('h6#song_artist').text(),track_name:$('h5#song_title').text()}),
        success: function(response) {
          $('#my_container').html(response);
        },
        contentType: 'application/json;charset=UTF-8'
      });
      return false;
    });
});
