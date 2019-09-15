let cores = [1,2,2,3,3,2,2,0,0,2,2,1,1,0,0,2,2,1,1,3,3,1,1,0,0,2,2,0,0,2,2,0,0,2,2,0,0,2,2,0,0,2,2,0,0,1,1,3,3,1,1,0,0,1,1,3,3,0,0,1];
let i = 0;
function setup(){
    createCanvas(windowWidth, windowHeight)
    fill(255,0,0);
    a = ellipse(windowWidth/8, windowHeight/2, 100, 100);
    fill(0);
    textSize(32);
    text("Core 0", windowWidth/8 - 50, 3*windowHeight/4);
    fill(250,0,0);
    b = ellipse(windowWidth/3, windowHeight/2, 100, 100);
    fill(0);
    textSize(32);
    text("Core 1", windowWidth/3 - 50, 3*windowHeight/4);
    fill(250,0,0);
    c = ellipse((windowWidth/2), (windowHeight/2), 100, 100);
    fill(0);
    textSize(32);
    text("Core 2", windowWidth/2 - 50, 3*windowHeight/4);
    fill(250,0,0);
    d = ellipse(windowWidth/1.4, windowHeight/2, 100, 100);
    fill(0);
    textSize(32);
    text("Core 3", windowWidth/1.4 - 50, 3*windowHeight/4);
    frameRate(3);
}

function draw(){
    background(255,255,255);
        if(i>cores.length){
            fill(0);
            textSize(32);
            text("End of data reached, resetting now.", 10, 30);
            i = 0;

        }
        else{
        fill(0);
        textSize(32);
        text('Core ID: '+String(cores[i]), 10, 30);
        text('4 core processor.', 10, 80);
        text('Average time thread ran on each core: 4.666 milliseconds', 10, 130);
                
        if(cores[i]==0){
            fill(0,0,0);
            a = ellipse(windowWidth/8, windowHeight/2, 100, 100);
            fill(0);
            textSize(32);
            text("Core 0", windowWidth/8 - 50, 3*windowHeight/4);
            fill(250,0,0);
            b = ellipse(windowWidth/3, windowHeight/2, 100, 100);
            fill(0);
            textSize(32);
            text("Core 1", windowWidth/3 - 50, 3*windowHeight/4);
            fill(250,0,0);
            c = ellipse((windowWidth/2), (windowHeight/2), 100, 100);
            fill(0);
            textSize(32);
            text("Core 2", windowWidth/2 - 50, 3*windowHeight/4);
            fill(250,0,0);
            d = ellipse(windowWidth/1.4, windowHeight/2, 100, 100);
            fill(0);
            textSize(32);
            text("Core 3", windowWidth/1.4 - 50, 3*windowHeight/4);
        }
        else if(cores[i]==1){
            fill(255,0,0);
            a = ellipse(windowWidth/8, windowHeight/2, 100, 100);
            fill(0);
            textSize(32);
            text("Core 0", windowWidth/8 - 50, 3*windowHeight/4);
            fill(0,0,0);
            b = ellipse(windowWidth/3, windowHeight/2, 100, 100);
            fill(0);
            textSize(32);
            text("Core 1", windowWidth/3 - 50, 3*windowHeight/4);
            fill(250,0,0);
            c = ellipse((windowWidth/2), (windowHeight/2), 100, 100);
            fill(0);
            textSize(32);
            text("Core 2", windowWidth/2 - 50, 3*windowHeight/4);
            fill(250,0,0);
            d = ellipse(windowWidth/1.4, windowHeight/2, 100, 100);
            fill(0);
            textSize(32);
            text("Core 3", windowWidth/1.4 - 50, 3*windowHeight/4);
        }
        else if(cores[i]==2){
            fill(255,0,0);
            a = ellipse(windowWidth/8, windowHeight/2, 100, 100);
            fill(0);
            textSize(32);
            text("Core 0", windowWidth/8 - 50, 3*windowHeight/4);
            fill(250,0,0);
            b = ellipse(windowWidth/3, windowHeight/2, 100, 100);
            fill(0);
            textSize(32);
            text("Core 1", windowWidth/3 - 50, 3*windowHeight/4);
            fill(0,0,0);
            c = ellipse((windowWidth/2), (windowHeight/2), 100, 100);
            fill(0);
            textSize(32);
            text("Core 2", windowWidth/2 - 50, 3*windowHeight/4);
            fill(250,0,0);
            d = ellipse(windowWidth/1.4, windowHeight/2, 100, 100);
            fill(0);
            textSize(32);
            text("Core 3", windowWidth/1.4 - 50, 3*windowHeight/4);
        }
        else if(cores[i]==3){
            fill(255,0,0);
            a = ellipse(windowWidth/8, windowHeight/2, 100, 100);
            fill(0);
            textSize(32);
            text("Core 0", windowWidth/8 - 50, 3*windowHeight/4);
            fill(250,0,0);
            b = ellipse(windowWidth/3, windowHeight/2, 100, 100);
            fill(0);
            textSize(32);
            text("Core 1", windowWidth/3 - 50, 3*windowHeight/4);
            fill(250,0,0);
            c = ellipse((windowWidth/2), (windowHeight/2), 100, 100);
            fill(0);
            textSize(32);
            text("Core 2", windowWidth/2 - 50, 3*windowHeight/4);
            fill(0,0,0);
            d = ellipse(windowWidth/1.4, windowHeight/2, 100, 100);
            fill(0);
            textSize(32);
            text("Core 3", windowWidth/1.4 - 50, 3*windowHeight/4);
        }
        i++;
    }

}


var myArray = new Array(3);
for(i=0;i<)