from django.shortcuts import render, redirect
from .forms import ResumeForm


def index(request):
    error = ''
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home2')
        else:
            error = 'Форма была неверной'
    form = ResumeForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'mainn/html/index.html', data)