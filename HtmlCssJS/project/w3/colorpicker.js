function doLime(){
    var d1=document.getElementBYId("c1");
    d1.style.backgroundColor="lime";
}
function docolor(){
    var d2=document.getElementById("c1");
    var colorinput = document.getElementById("clr");
    var color = colorinput.value;
    d2.style.backgroundColor= color;
}
function dosquare(){
    var d3 =document.getElementById("c1");
    var sizeinput=document.getElementById("sldr");
    var size=sizeinput.value;
    var ctx=d3.getContext("2d");
    ctx.clearRect(0,0,d3.Width,d3.height);
    ctx.fillStyle="yellow";
    ctx.fillRect(10,10,size,size);

}