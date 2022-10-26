
from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog

# Create your views here.

def blog_list(request):
    return HttpResponse("연결 확인")