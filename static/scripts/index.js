var btn = $(".file_button_container");
var loading = $("#loading");

$("input").mouseenter(function(){
  btn.css("filter","invert(70%)");
  btn.css("filter","invert(70%)");
})
$("input").mouseleave(function(){
  btn.css("filter","invert(50%)");
  btn.css("filter","invert(50%)");
})
rotate = 0;
setInterval(function(){
  loading.css("filter","hue-rotate("+rotate+"deg)");
  loading.css("-webkit-filter","hue-rotate("+rotate+"deg)");
  rotate = rotate + 5;
},50)

function doUpload(fm){
  fm.submit();
  loading.show();
  $(".form-container").hide();
  $(".text").hide();
}
