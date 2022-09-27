$(function(){

    const button = document.querySelector('.events_slider_sign_up');
    const button_sign_up = document.querySelector('#pop_up_sign_up');
    const button_sign_up1 = document.querySelector('#pop_up_sign_up1');
    const form = document.querySelector('#description_form');
    const popup = document.querySelector('.popup');
    const popup1 = document.querySelector('.popup1');
    const popup__container = document.querySelector('.popup__container');
    var popup__container_onclick = new Boolean(true);
    const form_sign_up = document.querySelector('#description_form_sign_up');
    const popup_sign_up = document.querySelector('.popup_sign_up');
    const popup__container_sign_up = document.querySelector('.popup__container_sign_up');
    var popup__container_onclick_sign_up = new Boolean(true);
    const second = document.querySelector('#second');
    popup.style="display: none";
    popup1.style="display: none";
    popup_sign_up.style="display: none";



    button.addEventListener('click', () => {
      popup.style="display: block";
    });


    button_sign_up.addEventListener('click', () => {
      popup.style="display: none";
      popup_sign_up.style="display: block";
    });

    popup1.addEventListener('click', function Close(event) {
        if (event.target == this){
              popup1.style="display: none";
              popup_sign_up.style="display: none";
              }
              console.log(3);
    });











    second.addEventListener('click', () => {
      popup1.style="display: block";
    });

    button_sign_up1.addEventListener('click', () => {
      popup1.style="display: none";
      popup_sign_up.style="display: block";
    });



    popup_sign_up.click(function(event){

        console.log(6);
            popup_sign_up.style="display: none";

    });



    popup_sign_up.addEventListener('click', function Close(event) {
    if (event.target == this){
          popup.style="display: none";
          popup_sign_up.style="display: none";
          }
    });

    popup.addEventListener('click', function Close(event) {
    if (event.target == this){
          popup.style="display: none";
          popup_sign_up.style="display: none";
          }
          console.log(3);
    });

});


