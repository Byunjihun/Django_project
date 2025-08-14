# articles/admin.py

from django.contrib import admin
from .models import Article   # <-- 앞에 점(.)을 추가하여 같은 폴더를 지정합니다.

admin.site.register(Article)