
var title = document.getElementById("titleCharts");
var containerTitle = document.getElementById("titleCharts");
var im = document.getElementById("loadingScheme");

function showWeight(){
    im.style.display = "none";
    containerTitle.style.backgroundColor= document.getElementById("weght").style.backgroundColor;
    document.getElementById("HRate").style.display = "none";
    document.getElementById("nrStp").style.display = "none";
    document.getElementById("weght").style.display = "block";
    document.getElementById("foods").style.display = "none";
    title.textContent ="Peso";
    getDataFitbitWeight("sum text Weight");
}
function showHR(spectrum){    
    im.style.display = "none";
    containerTitle.style.backgroundColor= document.getElementById("HRate").style.backgroundColor;
    document.getElementById("HRate").style.display = "block";
    document.getElementById("nrStp").style.display = "none";
    document.getElementById("weght").style.display = "none";
    document.getElementById("foods").style.display = "none";
    title.textContent ="Actividad Cardiaca";
    getDataFitbitCharts("HR",spectrum);
}
function showSteps(spectrum){
    im.style.display = "none";
    containerTitle.style.backgroundColor= document.getElementById("nrStp").style.backgroundColor;
    document.getElementById("HRate").style.display = "none";
    document.getElementById("nrStp").style.display = "block";
    document.getElementById("weght").style.display = "none";
    document.getElementById("foods").style.display = "none";
    title.textContent ="Pasos";
    getDataFitbitCharts("ST",spectrum);
}
function showFood(spectrum){
    im.style.display = "none";
    containerTitle.style.backgroundColor= document.getElementById("foods").style.backgroundColor;
    document.getElementById("HRate").style.display = "none";
    document.getElementById("nrStp").style.display = "none";
    document.getElementById("weght").style.display = "none";
    document.getElementById("foods").style.display = "block";
    title.textContent ="Comidas";
    getDataFitbitFoods("alers",spectrum); 
}

