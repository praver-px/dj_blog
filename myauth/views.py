import random
import string

from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def send_email_captcha(request):
    email = request.GET.get('email')
    if not email:
        return JsonResponse({'code': 400, 'message': '请输入邮箱'})

    # 生成验证码(6位随机数)
    captcha = ''.join(random.sample(string.digits, 6))
    send_mail('验证码', message=f'你的验证码为{captcha}', recipient_list=[email], from_email=None)
    return JsonResponse({'code': 200, 'message': '发送成功'})
