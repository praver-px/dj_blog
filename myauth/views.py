import random
import string

from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from myauth.forms import RegisterForm
from myauth.models import CaptchaModel
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.


def login(request):
    return render(request, 'login.html')


@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            User.objects.create_user(email=email, username=username, password=password)
            return redirect(reverse('myauth:login'))
        else:
            print(form.errors)
            return redirect(reverse('myauth:register'))
            # return render(request, 'register.html', context={'form': form})


def send_email_captcha(request):
    email = request.GET.get('email')
    if not email:
        return JsonResponse({'code': 400, 'message': '请输入邮箱'})

    # 生成验证码(6位随机数)
    captcha = ''.join(random.sample(string.digits, 6))
    CaptchaModel.objects.update_or_create(email=email, defaults={'captcha': captcha})
    send_mail('验证码', message=f'你的验证码为{captcha}', recipient_list=[email], from_email=None)
    return JsonResponse({'code': 200, 'message': '发送成功'})
