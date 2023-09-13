from . import views
from django.urls import path
app_name = 'post'

urlpatterns = [
 path('postlogin',views.postlogin,name='postlogin'),
 path('create/', views.create_post, name='create_post')


]