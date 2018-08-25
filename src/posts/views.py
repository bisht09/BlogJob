from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.
def post_create(request, *args, **kwargs):
	return HttpResponse("<h1>Create</h1>")

def post_detail(request, *args, **kwargs):
	obj = get_object_or_404(Post, id=3)
	context = {
		"title" : "Detail",
		"instance": obj,
	}
	return render(request, "post_detail.html", context)

def post_list(request, *args, **kwargs):
	queryset = Post.objects.all()
	context = {
		"title" : "Lists",
		"object_list" : queryset,
	}
	return render(request, "index.html", context)

def post_update(request, *args, **kwargs):
	return HttpResponse("<h1>Update</h1>")

def post_delete(request, *args, **kwargs):
	return HttpResponse("<h1>Delete</h1>")