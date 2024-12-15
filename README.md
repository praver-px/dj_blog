# django 学习-项目实战（前后端不分离）

> 来源 [知了blog](https://www.bilibili.com/video/BV1N1421U76L/?p=41)

## 静态文件

```python
## setting.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            # 加载静态文件
            'builtins': ['django.templatetags.static'],
        },
    },
]

STATIC_URL = 'static/'
# 静态文件目录
STATICFILES_DIRS = [BASE_DIR / 'static']

```

