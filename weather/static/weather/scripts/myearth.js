$( document ).ready(function() {
    console.log( "ready!" );
});


$.getJSON("{% static 'weather/scripts/forecasts.json' %}",function(data){
console.log(data);
var output = '<ul>';
$.each(data, function(key,val){
  output += '<li>'+ val.pv_estimate + " " + val.period_end + '</li>';
});
output += '</ul>';
$('#advice').html(output);
});
