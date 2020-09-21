from django.urls import path
from bookmark.views import BookmarkLV, BookmarkDV

app_name = 'bookmark'
urlpatterns = [
    # url패턴의 이름 => bookmark:index
    path('', BookmarkLV.as_view(), name='index'),
    # url패턴의 이름 => bookmark:detail
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
]
