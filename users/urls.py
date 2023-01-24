from django.urls import path
from users import views

urlpatterns = [
    path('engineer', views.Jobs.as_view()),
]