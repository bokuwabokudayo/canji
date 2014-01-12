function write(){
	var i=0;
      while(i<10){
        document.write("繰り返し"+(i+1)+"回目<br>");
        i=i+1;
      }
        document.write("テストです");
	document.close();
}

onload = function() {
  status_online();
};

function status_online() {
  var canvas = document.getElementById("status_online");
  if ( ! canvas || ! canvas.getContext ) {
  	return false;
  }
  var ctx = canvas.getContext("2d");
  ctx.beginPath();
  ctx.fillStyle = 'rgb(126, 211, 33)';
  ctx.arc(6, 6, 6, 0, Math.PI*2, false);
  ctx.fill();
}