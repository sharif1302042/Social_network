from django.urls import path
from chat import views

urlpatterns = [
    #path('<room_name>/', views.ChatView.as_view(), name='chat'),
    path('<room_name>/', views.room, name='chat'),
]
