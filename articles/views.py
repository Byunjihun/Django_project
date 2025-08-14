from django.shortcuts import render
# django가 가지고 있는 http에 따른 응답 방식
from django.http import JsonResponse
# Restful한 API를 만들도록 해주는 framwork
from rest_framework.decorators import api_view 

# 행위 -> Rsetful API를 위한 것
# @api_view(['GET', 'POST']) 데코레이터에 의해 이 함수는 GET 또는 POST 요청에만 응답하도록 설정됩니다.
# if request.method == 'POST' 또는 elif request.method == 'GET' 코드를 통해 사용자가 어떤 방식(POST 또는 GET)으로 요청했는지 확인합니다.
# 어떤 방식의 요청이든 상관없이, 'message': 'Hello,Django!'라는 데이터를 담은 JsonResponse 객체를 반환합니다.
# 최종 응답: Django는 이 JsonResponse를 사용자에게 전송합니다. 사용자는 JSON 형태의 { "message": "Hello,Django!" } 응답을 받게 됩니다.
@api_view(['GET','POST'])
def index(request):
    # 모든 view 함수는 첫 번째 인자에 request가 고정되어 있습니다.
        # 인자명 request는 다른 이름이어도 상관은 없지만 django 가이드 상, request이므로 다른 이름으로 적지는 않습니다.

    # request에는 사용자의모든 요청과 관련된 정보가 담겨 있습니다.
    if request.method == 'POST':
        return JsonResponse({'message':'Hello,Django!'})
    elif request.method == 'GET':
        return JsonResponse({'message':'Hello,Django!'})

def detail(request, article_pk):
    # 원래는 http://.../articles/5/)에 요청이 들어오면 여기서 model을 거쳐서 실제 5번 게시글을 가져와야 하는데
    # 지금은 모델이 없으니 그냥 반환하도록 합니다.
    
    # detail(request, article_pk) 함수가 호출되며, article_pk 값으로 5가 들어옵니다.
    # data = {'id': 5, 'message': '5번 게시글에 대한 정보입니다.'} 와 같이 article_pk 값을 활용한 딕셔너리를 생성합니다.
    # 이 data를 담아 JsonResponse 객체를 반환합니다.
    data = {
        'id' : article_pk,
        'message' : f'{article_pk}번 게시글에 대한 정보입니다.'
    }

    # 최종 응답: Django는 이 JsonResponse를 사용자에게 전송합니다. 사용자는 JSON 형태의 { "id": 5, "message": "5번 게시글에 대한 정보입니다." } 응답을 받게 됩니다.
    return JsonResponse(data)