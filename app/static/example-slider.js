
var examples_folder="/static/examples/";
var outputs_folder=examples_folder.concat("output/");
var images=["sony-20005-x6.png","fuji-20167-x8.png","fuji-20184-x1.png", "sony-20020-x6.png",
            "sony-20177-x12.png", "sony-20201-x4.png",];
            /*"sony-20005-x6.jpg","fuji-20167-x8.jpg","fuji-20184-x1.jpg", "sony-20020-x6.jpg",
            "sony-20177-x12.jpg", "sony-20201-x4.jpg",];*/

// Número de la imagen que se muestra
var num = 0;

// Pasar a imagen previa
function prev(){
    num--;
    if(num<0){
	    num = images.length-1;
    }
    document.getElementById("example-input").src = examples_folder.concat(images[num]);
    document.getElementById("example-output").src = outputs_folder.concat(images[num]);
}

// Pasar a imagen siguiente
function next(){
    num++;
    if(num>=images.length){
	    num = 0;
    }
    document.getElementById("example-input").src = examples_folder.concat(images[num]);
    document.getElementById("example-output").src = outputs_folder.concat(images[num]);
}

document.getElementById("example-input").src = examples_folder.concat(images[num]);
document.getElementById("example-output").src = outputs_folder.concat(images[num]);

