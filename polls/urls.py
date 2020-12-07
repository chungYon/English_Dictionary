from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:word_id>/', views.detail, name='detail'),
    path('results/', views.results, name='results'),
    path('<str:word_text>/', views.detail_str, name='detail_str'),
]

app_name = 'polls'
