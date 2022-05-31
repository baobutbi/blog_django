from django.shortcuts import render
from h11 import Data
from .models import Post
def contact(request):
   return render(request, 'pages/contact.html')
def list(request):
   Data = {'Post': Post.objects.all().order_by("-date")}
   return render(request,'blog/blog.html',Data)
def post(request, id):
   post = Post.objects.get(id=id)
   return render(request, 'blog/post.html', {'post': post})