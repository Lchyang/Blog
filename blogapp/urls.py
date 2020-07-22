from django.urls import path
from blogapp import views

app_name = 'blogapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:pk>', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('categories/<int:pk>/', views.category, name='category'),
    path('tags/<int:pk>/', views.tag, name='tag'),
]
