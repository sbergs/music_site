
$(document).ready(function() {
  // Handler for .ready() called.

  audiojs.events.ready(function() {
    var as = audiojs.createAll();
  });

  // removed time for now will probbaly add back in
  var formatTime = function (length) {
    //length is in ms
    var minutes = length/60000;
    var seconds = Math.round((minutes - Math.floor(minutes)) * 60);
    if( String(seconds).length === 1)
        seconds = seconds + "0";

    return Math.floor(minutes) + ":" + seconds;
  };

  $(document).on("click", "a", function(){
    event.preventDefault();

    var trackHTML = '<ul class="small-block-grid-1">'

    $.getJSON($(this).attr('href'), function(data){
        var trackCount = data.length - 1;
        for (var i = trackCount; i >= 0; i--) {
            trackHTML = trackHTML + '<li>' + data[i].fields.name +'</li>';
        }

        trackHTML = trackHTML + '</ul>';
        $("#trackbrowser").html(trackHTML);

    });
 });
});
