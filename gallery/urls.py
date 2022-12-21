from django.urls import path
from. import views
from common import views as common_views

app_name = 'gallery'

urlpatterns = [
    path('<int:user_id>/', views.gallery, name='gallery'),
    path('detail/<int:artwork_id>/', views.detail, name='detail'),
    path('upload/', views.artwork_upload, name='artwork_upload'),
    path('modify/<int:artwork_id>/', views.artwork_modify, name='artwork_modify'),
    path('delete/<int:artwork_id>/', views.artwork_delete, name='artwork_delete'),
    path('explore/', views.explore, name='explore'),
    path('detail/<int:artwork_id>/likes/', views.artwork_likes, name='artwork_likes'),
    path('detail/<int:artwork_id>/comment/create/', views.comment_create, name='comment_create'),
    path('detail/<int:comment_id>/comment/modify/', views.comment_modify, name='comment_modify'),
    path('detail/<int:comment_id>/comment/delete/', views.comment_delete, name='comment_delete'),
    
]
