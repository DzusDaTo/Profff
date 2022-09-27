$(function(){
    const begin = document.querySelector('#begin');
    const anketa = document.querySelector('#anketa');
    const anons = document.querySelector('#anons');

    begin.addEventListener('click', () => {
        console.log("works!")
        anketa.style.display='block';
        anons.style.display='none';
    });


});