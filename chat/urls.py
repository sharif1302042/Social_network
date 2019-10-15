from django.urls import path
from chat import views

urlpatterns = [
    path('<room_name>/', views.Chat.as_view(), name='chat'),
]
