from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_http_methods

from blog.forms import PubBlogForm
from blog.models import BlogCategory, Blog


# Create your views here.


def index(request):
    return render(request, 'index.html')


def blog_detail(request, blog_id):
    return render(request, 'blog_detail.html')


@require_http_methods(['GET', 'POST'])
@login_required(login_url=reverse_lazy('myauth:login'))
def pub_blog(request):
    if request.method == 'GET':
        category = BlogCategory.objects.all()
        return render(request, 'pub_blog.html', context={'category': category})
    else:
        form = PubBlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            category_id = form.cleaned_data.get('category')
            blog = Blog.objects.create(title=title, content=content, author=request.user, category_id=category_id)
            return JsonResponse({'code': 200, 'message': '发布成功', "data": {'blog_id': blog.id}})
        else:
            print(form.errors)
            return JsonResponse({'code': 400, 'message': form.errors})
