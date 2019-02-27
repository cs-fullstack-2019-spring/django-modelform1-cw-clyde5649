from django.shortcuts import render
from django.http import HttpResponse
from .forms import BlogPostForm
# Create your views here.

def index(request):
    return render('blgapp/index.html')

def Blogs(request):
    blogs_Forms = BlogPostForm()





