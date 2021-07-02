//Write a function named setBlack that has one parameter pixel (representing a single pixel) and returns pixel with its red, green, and blue components changed so that the pixel’s color is black. Now you will write another function named addBorder. This function will add a black border to an image that is 10 pixels thick.

var img = new SimpleImage("SmallPanda.png");
var xBound = img.getWidth()-10;
var yBound = img.getHeight()-10;

function setBlack (p){
    p.setRed(0);
    p.setBlue(0);
    p.setGreen(0);
}

for (var pixel of img.values()){
  if (pixel.getX()<=10 || pixel.getX()>=xBound)
      setBlack(pixel);
      
  if (pixel.getY()<=10 || pixel.getY()>=yBound)
      setBlack(pixel);
  
}
print (img);