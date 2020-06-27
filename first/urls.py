from django.conf.urls import url
from first import views
from django.urls import path,include

app_name = "first"

urlpatterns = [
    url(r'^$', views.index,name='index'),
    path('upload', views.upload_image,name='upload_image'),
]