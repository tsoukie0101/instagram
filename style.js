let i = 0
let color = ["#4DCCFF", "#FF9156", "#5F67EC", "#F67162", "#0E3854", "#067EED", "#FF7C1F" ]
let btn = document.getElementById('btn');
btn.addEventListener('click', changeColor);

function changeColor(){ 
    if(i< color.length){
        document.getElementById('corps').style.backgroundColor = color[i];
        i++;
    }else{
        document.getElementById('corps').style.backgroundColor = "#283747";
        i = 0;
    };

}; 