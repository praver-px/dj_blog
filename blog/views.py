from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy


# Create your views here.


def index(request):
    return render(request, 'index.html')


def blog_detail(request, blog_id):
    return render(request, 'blog_detail.html')


@login_required(login_url=reverse_lazy('myauth:login'))
def pub_blog(request):
    return render(request, 'pub_blog.html')
