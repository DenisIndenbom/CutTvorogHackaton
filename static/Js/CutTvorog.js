let rost = 100
function f() {
    let id1 = document.getElementById('voloses1');
    let idbuton = document.getElementById('button');
    let pos = 43;
    let id = setInterval(farm,rost);
    function farm() {
        if(pos === 49){
            clearTimeout(id);
            f1();
            idbuton.classList.add('extibutton');

        }else{
            pos+=1;
            id1.style.width = pos + 'vw';

        }
    }
}

f();
n = 0
function f1() {
    n+=6;
    console.log('lol');
    let element = document.createElement('img');
    let body= document.getElementById('body');
    element.src = "static/img/tvorog1.png";
    element.position = "absolute";
    element.top = n;
    body.appendChild(element);
    let pos = 42;
    let id = setInterval(farm,rost);
    function farm() {
        if(pos === 49){
            clearTimeout(id);
            f1();
        }else{
            pos+=1;
            element.style.width = pos + 'vw';
        }
    }


}