from django.urls import path
from users import views

urlpatterns = [
    path('engineer', views.ListApi.as_view()),
]