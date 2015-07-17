from django.shortcuts import render
from myblog.models import MyBlog
from django.shortcuts import render_to_response
# Create your views here.

def blogs(request):
    return render_to_response('blogs.html', {'blogs':MyBlog.objects.all()})

def blog(request,myblog_id=1):
    return render_to_response('blog.html', {'blog':MyBlog.objects.get(id=myblog_id)})