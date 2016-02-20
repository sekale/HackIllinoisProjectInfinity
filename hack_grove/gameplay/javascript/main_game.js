// Create the canvas
var canvas = document.createElement("canvas");
var ctx = canvas.getContext("2d");
var screen_width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
var screen_height = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;;
var canvas_padding = 10;

var directionDriving = "CENTER";

var test_player_x, test_player_y;

console.log(screen_width);
setup();
main();


function setup()
{
    console.log("start setup");
    canvas.width =  screen_width - canvas_padding;
    canvas.height = screen_height - canvas_padding;
    document.body.style.backgroundColor = "blue";
    document.body.appendChild(canvas);

    test_player_x = canvas.width/ 2;
    test_player_y = canvas.height/ 2;
}

function main()
{
    ctx.fillStyle = "rgba(255,0,0,1)";
    ctx.fillRect(0,0, canvas.width, canvas.height);
    //ctx.stroke();
    ctx.fillStyle = "rgba(0,0,0,1)";
    ctx.rect(test_player_x,test_player_y, 50, 50);
    ctx.stroke();
    console.log("yo");
    if(directionDriving == "LEFT")
        test_player_x -= 1;
    else if(directionDriving == "RIGHT")
        test_player_x += 1;
    requestAnimationFrame(main);
}

document.getElementById("lr_action").onchange = function()
{
    directionDriving = document.getElementById("lr_action").value;
    console.log("lr_action was changed to " + directionDriving);
};
