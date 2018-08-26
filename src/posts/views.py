from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
# Create your views here.
def post_create(request, *args, **kwargs):
	form = PostForm(request.POST or None)
	context = {
		"form" : form
	}
	if form.is_valid():
		form.save()
		form = PostForm()
		context = {
			"form":form,
			"message" : "The post was successfully created"
		}
	return render(request, "post_create.html", context)

def post_detail(request, id, *args, **kwargs):
	obj = get_object_or_404(Post, id=id)
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