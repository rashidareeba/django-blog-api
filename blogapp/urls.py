from django.urls import path
from .views import (
    PostListCreate,
    PostDetail,
    CommentCreate,
    CommentDelete,
    TagList,
    PostsByTag
)

app_name = 'api'  


urlpatterns = [
    path('posts/', PostListCreate.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', CommentCreate.as_view(), name='comment-create'),
    path('comments/<int:pk>/', CommentDelete.as_view(), name='comment-delete'),
    path('tags/', TagList.as_view(), name='tag-list'),
    path('tags/<int:tag_id>/posts/', PostsByTag.as_view(), name='posts-by-tag'),
]