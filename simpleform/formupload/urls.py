from django.conf.urls import url, include
from formupload import views
 
urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^upload/', views.upload, name="upload"),
]
