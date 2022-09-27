from django.shortcuts import render
from django.views.generic import DetailView
from .models import Resumeout


def news_out(request):
    news_home = Resumeout.objects.order_by('-date')
    return render(request, 'resumeout/html/news_out1.html', {'news_home': news_home})


class NewsDetailView(DetailView):
    model = Resumeout
    template_name = 'resumeout/html/detail_view1.html'
    context_object_name = 'resumeout'