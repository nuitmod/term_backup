from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'void/', views.index, name='void'),
    url(r'main_v/', views.ind_main, name='ind_main'),
    url(r'form/', views.form, name='form'),
]
