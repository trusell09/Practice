var count=1;
var countElement = document.querySelector ("#likes");

console.log(countElement);

function add1(){
    count ++;
    countElement.innerText = count + "like(s)";
    console.log(count);
} 



var count2=1;
var countElement2 = document.querySelector ("#likes2");

console.log(countElement2);

function add2(){
    count2 ++;
    countElement2.innerText = count2 + "like(s)";
    console.log(count2);
}


var count2=1;
var countElement2 = document.querySelector ("#likes2");

console.log(countElement2);

function unlike(){
    count2 --;
    countElement2.innerText = count2 + "like(s)";
    console.log(count2);
} 


