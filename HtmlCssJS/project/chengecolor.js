var img = new SimpleImage(200,200);
print(img);
for (var pixel of img.values()){
    pixel.setGreen(255)
    pixel.setRed(255)
    pixel.setBlue(0)
}
print(img)