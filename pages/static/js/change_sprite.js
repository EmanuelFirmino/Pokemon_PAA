var element = document.getElementById('pokemon');
console.log(element);

setInterval(() => {
    var num = Math.floor(Math.random() * 900) + 1;
    var pokes = '../static/sprites/' + num + '.png';
    element.setAttribute('src', pokes);
    console.log(num);    
}, 1500);

var element_mobile = document.getElementById('pokemon_mobile');
console.log(element_mobile);

setInterval(() => {
    var num = Math.floor(Math.random() * 900) + 1;
    var pokes = '../static/sprites/' + num + '.png';
    element_mobile.setAttribute('src', pokes);
    console.log(num);    
}, 1500);