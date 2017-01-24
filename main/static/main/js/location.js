function init_map(){
    var myOptions = {zoom:15,center:new google.maps.LatLng(54.767249,  -1.570387),mapTypeId: google.maps.MapTypeId.ROADMAP};
    map = new google.maps.Map(document.getElementById("gmap-canvas"), myOptions);
    marker = new google.maps.Marker({map: map,position: new google.maps.LatLng(54.767249,  -1.570387)});
    infowindow = new google.maps.InfoWindow({
        content: '<div class="map-pointer"><strong>School of Engineering<br>and Computing Sciences</strong><br>Durham University</div>',
        maxWidth: 150
    });
    google.maps.event.addListener(marker, "click", function(){infowindow.open(map,marker);});
    infowindow.open(map,marker);
}
google.maps.event.addDomListener(window, 'load', init_map);
