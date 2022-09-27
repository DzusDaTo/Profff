function openBlock(id, btn){
    elem = document.getElementById(id); //находим блок div по его id, который передали в функцию
    btn_ = document.getElementById(btn); //находим блок div по его id, который передали в функцию
    state = elem.style.display; //смотрим, включен ли сейчас элемент
    if (state =='') {
        elem.style.display='none'; //если включен, то выключаем
        btn_.firstChild.data = "Ещё";
        
    } //если включен, то выключаем
    else {
        elem.style.display=''; //иначе - включаем
        btn_.firstChild.data = "Скрыть";
    }

        
}