/**
 * @Author: OUSMANE M. Sadjad <sadjad>
 * @Date:   2016-05-24T15:21:54+01:00
 * @Email:  ousmanesadjad@gmail.com
* @Last modified by:   sadjad
* @Last modified time: 2016-05-24T17:09:44+01:00
 */
function init_map() {
    var var_location = new google.maps.LatLng(6.354313, 2.396694);
    var var_mapoptions = {
        center: var_location,
        zoom: 15
    };

    var var_marker = new google.maps.Marker({
        position: var_location,
        map: var_map,
        title: "IRGIB Africa University"
    });

    var var_map = new google.maps.Map(document.getElementById("map-container"),
        var_mapoptions);

    var_marker.setMap(var_map);

}

google.maps.event.addDomListener(window, 'load', init_map);
