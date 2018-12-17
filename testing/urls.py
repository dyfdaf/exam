from django.urls import path
from . import views

urlpatterns = [
    path('<int:list_pk>', views.testing_detail, name='testing_detail'),
    path('', views.testing_list, name='testing_list'),
    path('score_submit/', views.score_submit)
]