from django.urls import path
from blogapp.views import index
from blogapp.views import detail

app_name = 'blogapp'
urlpatterns = [
    path('', index),
    path('article/<int:pk>', detail, name='detail')
]
