function dolime(){
    var d1=document.getElementById("c1");
    d1.style.backgroundColor="lime";
}
function doyellow(){
    var d1= document.getElementById("c1");
    d1.style.backgroundColor="white";
  var ctx= d1.getContext("2d");
  ctx.fillStyle="yellow";
  ctx.fillRect(10,10,40,40);
  ctx.fillRect(60,10,40,40);
  
  ctx.fillStyle="black";
  ctx.font="30px Arial";
  ctx.fillText("Omkar",10,90)
  
}