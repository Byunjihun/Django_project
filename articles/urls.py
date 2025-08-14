from django.urls import path
# 나랑 같은 폴더의 views
from.import views

urlpatterns = [
    path('index/', views.index),
    path('<int:article_pk>/',views.detail)
]

# 경우 1: index/ 경로로 접속할 때 (예: http://.../articles/index/)
# URL 매칭: Django는 urls.py의 urlpatterns를 확인하고 path('index/', views.index)와 일치하는 것을 찾습니다.
# 뷰 함수 호출: views.py 파일에 있는 index 함수를 호출합니다. 이때 사용자의 요청 정보(Request)가 request라는 인자로 함께 전달됩니다.

# -----------------------------------------------------------------------------------------------------------------------------------------------

# 경우 2: 특정 게시글 경로로 접속할 때 (예: http://.../articles/5/)
# URL 매칭: Django는 urls.py의 urlpatterns를 확인하고 path('<int:article_pk>/', views.detail)와 일치하는 것을 찾습니다.
# URL의 <int:article_pk> 부분은 URL 경로에서 숫자를 추출하여 article_pk라는 이름의 변수로 만들어줍니다. 이 경우, '5'가 추출되어 정수 5가 됩니다.
# 뷰 함수 호출: views.py 파일에 있는 detail 함수를 호출합니다. 이때 사용자의 요청 정보(request)와 함께 URL에서 추출한 값 article_pk=5를 인자로 전달합니다.


