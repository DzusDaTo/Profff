var myInput = document.getElementById("password");
var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");
var passwordRepeat = document.getElementById("passwordRepeat");
var letter = document.getElementById("letter_span");
var capital = document.getElementById("capital_span");
var number = document.getElementById("number_span");
var length = document.getElementById("length_span");
var passwordRepeatCorrect = document.getElementById("passwordRepeatCorrect");
var eye = document.getElementById("eye");
var eyeRepeat = document.getElementById("eyeRepeat");
var s = '✔';
txt = document.createTextNode(s);

// Когда пользователь нажимает на поле пароль, появляется окно сообщения
myInput.onfocus = function() {
  document.getElementById("message").style.display = "block";
}

// Когда пользователь щелкает за пределами поля пароля, скройте окно сообщения
myInput.onblur = function() {
  document.getElementById("message").style.display = "none";
}

// Когда пользователь начинает вводить что-то в поле пароля
myInput.onkeyup = function() {
  // Проверка строчных букв
  var lowerCaseLetters = /[a-z]/g;
  if(myInput.value.match(lowerCaseLetters)) {
    letter.classList.remove("invalid");
    letter.classList.add("valid");
    letter.textContent = "✔		";
    letter.classList.remove("no");
    letter.classList.add("yes");
  }
  else {
    letter.classList.remove("valid");
    letter.classList.add("invalid");
    letter.textContent = "✘		";
    letter.classList.remove("yes");
    letter.classList.add("no");
  }

  // Проверка заглавных букв
  var upperCaseLetters = /[A-Z]/g;
  if(myInput.value.match(upperCaseLetters)) {
    capital.classList.remove("invalid");
    capital.classList.add("valid");
    capital.textContent = "✔		";
    capital.classList.remove("no");
    capital.classList.add("yes");
  }
  else {
    capital.classList.remove("valid");
    capital.classList.add("invalid");
    capital.textContent = "✘		";
    capital.classList.remove("yes");
    capital.classList.add("no");
  }

  // Проверка чисел
  var numbers = /[0-9]/g;
  if(myInput.value.match(numbers)) {
    number.classList.remove("invalid");
    number.classList.add("valid");
    number.textContent = "✔		";
    number.classList.remove("no");
    number.classList.add("yes");
  }
  else {
    number.classList.remove("valid");
    number.classList.add("invalid");
    number.textContent = "✘		";
    number.classList.remove("yes");
    number.classList.add("no");
  }

  // Проверка длины
  if(myInput.value.length >= 6) {
    length.classList.remove("invalid");
    length.classList.add("valid");
    length.textContent = "✔		";
    length.classList.remove("no");
    length.classList.add("yes");

  }
  else {
    length.classList.remove("valid");
    length.classList.add("invalid");
    length.textContent = "✘		";
    length.classList.remove("yes");
    length.classList.add("no");
  }



}

passwordRepeat.onkeyup = function()
{
    if(passwordRepeat.value == myInput.value)
      {
        passwordRepeatCorrect.style.display = "none";
      }
    else
    {
        passwordRepeatCorrect.style.display = "block";
        passwordRepeatCorrect.style.color = "red";
    }
}


eye.onclick = function()
{
    if(eye.classList.contains('fa-eye-slash')){
        eye.classList.remove('fa-eye-slash');
          eye.classList.add('fa-eye');
          myInput.setAttribute('type','text');

    }else{
        eye.classList.remove('fa-eye');
        eye.classList.add('fa-eye-slash');
        myInput.setAttribute('type','password');
    }
}

eyeRepeat.onclick = function()
{
    if(eyeRepeat.classList.contains('fa-eye-slash')){
        eyeRepeat.classList.remove('fa-eye-slash');
        eyeRepeat.classList.add('fa-eye');
          passwordRepeat.setAttribute('type','text');

    }else{
        eyeRepeat.classList.remove('fa-eye');
        eyeRepeat.classList.add('fa-eye-slash');
        passwordRepeat.setAttribute('type','password');
    }
}