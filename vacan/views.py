from django.shortcuts import render
from django.views.generic import DetailView
from .models import Vacan


def news_out1(request):
    news_home = Vacan.objects.order_by('-date')
    return render(request, 'vacan/html/news_out2.html', {'news_home': news_home})


class NewsDetailView(DetailView):
    model = Vacan
    template_name = 'vacan/html/detail_view2.html'
    context_object_name = 'vacan'
