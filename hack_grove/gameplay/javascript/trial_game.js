// Create the canvas
var canvas = document.createElement("canvas");
var ctx = canvas.getContext("2d");
canvas.width = 512;
canvas.height = 480;
document.body.style.backgroundColor = "yellow";
document.body.appendChild(canvas);


ctx.fillRect(20,20,150,100);
ctx.rect(40,40,250,200);
ctx.stroke();
