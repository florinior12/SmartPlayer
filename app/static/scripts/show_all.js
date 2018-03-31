$(document).ready(function() {
  $('#delete_all').click(function() {
   return false;
});

  $('a.play_id').click(function() {
    console.log('wewee');
    var button = $(this);
    player.loadVideoById(button.attr('id')); //get video id from url
    $('h5#song_title').text(button.closest('td').text());
    $('h6#song_artist').text(button.closest('tr').next().text());
    
    return false;
  });
});

