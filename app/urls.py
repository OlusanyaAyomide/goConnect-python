from django.urls import path
from . import views

urlpatterns=[
    path("",views.GetBase.as_view()),
    path("chats/<str:username>",views.GetUserChats.as_view()),
    path("chats/create/<str:username>",views.AskModelChat.as_view())
]