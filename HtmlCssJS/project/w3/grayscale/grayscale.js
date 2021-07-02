var imgIn;
var imgGray;

function upload() {
  /* Access Canvas 1: To Display Photo */
  var can1 = document.getElementById("c1");
  /* Access file input: Get filename from User */
  var fInput = document.getElementById("fileInput");

  /* Create a new SimpleImage from user entered Filename */
  imgIn = new SimpleImage(fInput);

  /* Create another SimpleImage with the same user entered */
  imgGray = new SimpleImage(fInput);

  /* Access Canvas 1 */
  var can1 = document.getElementById("c1");

  /* Display image on Canvas 1 */
  imgIn.drawTo(can1);
} 

/* Make a Global Grayscale copy of the Global Input Image */
function makeGray() {
  // For each pixel in the Grayscale Image
  for (var pix of imgGray.values()) {
    /* Calculate the average of the red, green and blue */
    var avg = (pix.getRed() + pix.getGreen() + pix.getBlue()) / 3;
    pix.setRed(avg);
    pix.setGreen(avg);
    pix.setBlue(avg);
  }

  // Access the second canvas to display the grayscale image
  var can2 = document.getElementById("c2");
  /* Display Image on Canvas 2 */
  imgGray.drawTo(can2);
}
