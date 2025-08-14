from django.contrib import admin 
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 자, 이제부터 'article/' 이라는 경로로 요청이 오게되면 
    # 이 요청들에 대해서는 articles 앱이 가진 urls가 처리!
    path('articles/', include('articles.urls'))
]

# 이 first_pjt/urls.py 파일의 역할은 프로젝트로 들어오는 모든 요청의 경로를 확인하고, 해당 요청을 처리할 담당자(앱)에게 전달하는 것입니다.

# 1. path('admin/', admin.site.urls)
# 경로: admin/

# 담당자: admin.site.urls

# 설명: http://.../admin/ 경로로 들어오는 요청은 Django의 내장된 관리자 페이지가 처리하도록 연결합니다. 이 경로는 Django 프로젝트를 만들 때 기본적으로 포함됩니다.

# 2. path('articles/', include('article.urls'))
# 경로: articles/

# 담당자: include('article.urls')

# 설명: 이 부분이 가장 핵심입니다.

# articles/: http://.../articles/와 같이 /articles/로 시작하는 모든 요청이 들어오면,

# include('article.urls'): include 함수를 사용하여 article 앱 폴더 안에 있는 urls.py 파일로 요청 처리를 위임합니다.

# 즉, articles와 관련된 모든 URL 요청은 이제 articles/urls.py 파일이 관리하게 됩니다. 이렇게 하면 프로젝트의 메인 urls.py 파일이 복잡해지는 것을 막고, 각 앱이 자신의 URL을 독립적으로 관리할 수 있게 됩니다.