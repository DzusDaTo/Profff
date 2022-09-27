const button = document.querySelector('.events_slider_sign_up');
const button_sign_up = document.querySelector('.pop_up_sign_up');
const form = document.querySelector('#description_form');
const popup = document.querySelector('.popup');
const popup__container = document.querySelector('.popup__container');
var popup__container_onclick = new Boolean(true);
const form_sign_up = document.querySelector('#description_form_sign_up');
const popup_sign_up = document.querySelector('.popup_sign_up');
const popup__container_sign_up = document.querySelector('.popup__container_sign_up');
var popup__container_onclick_sign_up = new Boolean(true);
console.log("1");



button_sign_up.addEventListener("mouseup", () => {
  if (form_sign_up.classList.contains('open_sign_up') && popup_sign_up.classList.contains('popup_open_sign_up'))
  {
    form_sign_up.classList.remove('open_sign_up');
    popup_sign_up.classList.remove('popup_open_sign_up');
    form_sign_up.classList.add('close_sign_up');
    popup_sign_up.classList.add('popup_close_sign_up');
  }
  form_sign_up.classList.remove('close_sign_up');
  popup_sign_up.classList.remove('popup_close_sign_up');
  form_sign_up.classList.add('open_sign_up');
  popup_sign_up.classList.add('popup_open_sign_up');
  form.classList.remove('open');
  popup.classList.remove('popup_open');
  form.classList.add('close');
  popup.classList.add('popup_close');

  console.log("Here!")
});


popup__container_sign_up.addEventListener('click', () => {
{
  popup__container_onclick_sign_up = true;
  console.log("popup__container_sign_up " + popup__container_onclick_sign_up);
} 
}); 

popup_sign_up.addEventListener('click', () => {
{
  if (popup__container_onclick_sign_up == false)
  {
    
    form_sign_up.classList.remove('open_sign_up');
    popup_sign_up.classList.remove('popup_open_sign_up');
    form_sign_up.classList.add('close_sign_up');
    popup_sign_up.classList.add('popup_close_sign_up');
    console.log("popup_sign_up FALSE " + popup__container_onclick_sign_up);
  }
  else 
  {
    popup__container_onclick_sign_up = false;
    console.log("popup_sign_up TRUE " + popup__container_onclick_sign_up);
    return;
  }
} 
}); 


  button.addEventListener('click', () => {
    if (form.classList.contains('open') && popup.classList.contains('popup_open'))
    {
      form.classList.remove('open');
      popup.classList.remove('popup_open');
      form.classList.add('close');
      popup.classList.add('popup_close');
    }
    form.classList.remove('close');
    popup.classList.remove('popup_close');
    form.classList.add('open');
    popup.classList.add('popup_open');
  });

  popup__container.addEventListener('click', () => {
    {
      popup__container_onclick = true;
      console.log("popup__containerp " + popup__container_onclick);
    } 
  }); 


  popup.addEventListener('click', () => {
    {
      if (popup__container_onclick == false)
      {
        form.classList.remove('open');
        popup.classList.remove('popup_open');
        form.classList.add('close');
        popup.classList.add('popup_close');
        console.log("popup FALSE " + popup__container_onclick);
      }
      else 
      {
        popup__container_onclick = false;
        console.log("popup TRUE " + popup__container_onclick);
        return;
      }
    } 
  }); 


