from django.shortcuts import render, redirect
from .forms import AbouttForm


def index(request):
    error = ''
    if request.method == 'POST':
        form = AbouttForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home1')
        else:
            error = 'Форма была неверной'
    form = AbouttForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'aboutt/html/index.html', data)


