from django.urls import path
from .views import *

urlpatterns = [
    # 클래스형 뷰, 함수형뷰를 path에 사용할 때 모양이 다르다
    # 함수형 뷰 : 뷰이름만 쓴다
    # 클래스형 뷰 : 뷰이름.as_view()
    # http://127.0.0.1:8000/bookmark/000.....
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    # Primary key
    path('detail/<int:pk>/', BookmarkUpdateView.as_view(), name='detail'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
    # int, str, slug, path
    # 필터 - Custom
]