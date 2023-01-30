var element = document.getElementById('pokemon');
console.log(element);

setInterval(() => {
    var num = Math.floor(Math.random() * 900) + 1;
    var pokes = '../static/sprites/' + num + '.png';
    element.setAttribute('src', pokes);
    console.log(num);    
}, 1500);