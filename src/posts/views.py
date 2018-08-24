from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def post_create(request, *args, **kwargs):
	return HttpResponse("<h1>Create</h1>")

def post_detail(request, *args, **kwargs):
	return HttpResponse("<h1>Detail</h1>")

def post_list(request, *args, **kwargs):
	return HttpResponse("<h1>List</h1>")

def post_update(request, *args, **kwargs):
	return HttpResponse("<h1>Update</h1>")

def post_delete(request, *args, **kwargs):
	return HttpResponse("<h1>Delete</h1>")