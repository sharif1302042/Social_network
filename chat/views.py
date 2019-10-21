import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class ChatView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'chat.html'
    def get(self,request,room_name):
        return Response({'room_name_json': mark_safe(json.dumps(room_name))},status = status.HTTP_200_OK)

    def post(self,request):
        return Response({'success_code':"success"},status = status.HTTP_200_OK)

@login_required
def room(request,room_name):
    return render(
        request,'chat.html',
    {
        'room_name_json':mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
    }
    )