from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('edit/<pk>/', views.EditComment.as_view(), name='update_comment'),
    path('delete/<pk>', views.DeleteComment.as_view(), name='delete_comment'),
]
