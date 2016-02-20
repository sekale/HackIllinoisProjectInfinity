// Create the canvas
var canvas = document.createElement("canvas");
var ctx = canvas.getContext("2d");
canvas.width = 512;
canvas.height = 480;
document.body.style.backgroundColor = "yellow";
document.body.appendChild(canvas);

var k = 30;

ctx.fillRect(20,20,150,100);
ctx.rect(0,0,canvas.width,canvas.height);
ctx.stroke();

document.getElementById("lr_action").onchange = function()
{
    console.log("yoyo");
    ctx.fillStyle = "rgba(0,0,0,1)";
    ctx.fillText(document.getElementById("lr_action").value, 0,0);
    console.log(document.getElementById("lr_action").value);
    ctx.rect(k,90,350,200);
    k += 10;
    ctx.stroke();
};

console.log("hello world");
