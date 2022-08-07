from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from accounts.models import Profile
from .models import BookCategory, Department, ContactUs, Blog, Comment, Newsletter
from .forms  import CommentUpdateForm
from django.views.generic import ListView,DetailView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import random

# Create your views here.

def home(request):
	blog=Blog.objects.all()
	if len(blog) !=0 and len (blog) >=3:
		blog=Blog.objects.all()[:2]

	return render (request, 'mainapp/index.html', {'blog':blog})

def about(request):
	return render (request, 'mainapp/about.html')

def blog(request):
	blogs=Blog.objects.all()
	return render (request, 'mainapp/blogs.html', {'blogs':blogs})

def blog_detail(request, slug):
	blog=Blog.objects.get(slug=slug)
	blogs=blog.user
	autor=Profile.objects.get(user=blogs)
	print(autor.bio) 
	latest=Blog.objects.all()[:4]
	comment=blog.comment_set.all()
	if request.method=='POST':
		if request.user.is_authenticated:
			_comment=Comment.objects.create(
				user=request.user,
				blog=blog,
				message=request.POST.get('message')

				)
			_comment.save()
		else:
			return redirect('login')
	return render (request, 'mainapp/blog.html', {'blog':blog, 'latest':latest, 'comment':comment})

def update_comment(request, pk):
	comment=Comment.objects.get(pk=pk)
	form=CommentUpdateForm(instance=comment)
	if request.method=="POST":
		form=CommentUpdateForm(request.POST,instance=comment)
		form.save()
		comment=comment.blog.slug
		return HttpResponseRedirect(reverse('_blog',args=[str(comment)]))
	return render(request, 'mainapp/update-comment.html', {'form':form})



def delete_comment(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	blog=comment.blog.slug
	if request.method=="POST":
		comment.delete()
		return HttpResponseRedirect(reverse('_blog',args=[str(blog)]))
	context={'obj':comment}
	return render(request, 'mainapp/update-comment.html', context)


def category(request):

	return render (request, 'mainapp/categories.html')


def geosciences(request):
	return render (request, 'mainapp/geosciences.html')

def years(request):
	return render (request, 'mainapp/years.html')

class DepartmentView(ListView):
	model=Department
	template_name='mainapp/departments.html'
	context_object_name='departments'


def dept_PQ_detail(request,slug):

	page='pq'
	dept=Department.objects.get(slug=slug)
	dept_detail= dept.bookcategory_set.filter(file_type='Past Questions')

	
	return render (request, 'mainapp/text_bk_detail.html', {'dept_detail':dept_detail, 'dept':dept, 'page':page})

def dept_TB_detail(request,slug):

	dept=Department.objects.get(slug=slug)
	dept_detail= dept.bookcategory_set.filter(file_type='Texts Books')

	page='tb'
	return render (request, 'mainapp/text_bk_detail.html', {'dept_detail':dept_detail, 'dept':dept, 'page':page})


def dept_HO_detail(request,slug):

	dept=Department.objects.get(slug=slug)
	dept_detail= dept.bookcategory_set.filter(file_type='Hand Outs')

	page='ho'
	return render (request, 'mainapp/text_bk_detail.html', {'dept_detail':dept_detail, 'dept':dept, 'page':page}) 


def contact(request):
	if request.method == "POST":

		contact=ContactUs.objects.create(
			name=request.POST.get('name'),
			email=request.POST.get('email'),
			phone_no=request.POST.get('phone_no'),
			message= request.POST.get('message'),
			)
		contact.save()
		# return redirect('subscribed')
		return render(request, 'mainapp/susbscribe.html')
	return render (request, 'mainapp/contact.html')


def search(request):
	# q=request.GET.get('q') if request.GET.get('q') !=None else ''
	if request.method== 'GET':
		q=request.GET.get('q') 
		if len(q)==0:
			return HttpResponse("<div class ='alert alert-primary' role ='alert'> A simple primary alert with <a href='' class='alert-link'>an example link</a>. Give it a click if you like.</div>")

	# else:
		
	books=BookCategory.objects.filter(title__icontains=q)
	return render(request, 'mainapp/text_bk_detail.html', {'books':books})

def newsletter(request):
	message='susbscribed'
	if request.method=='POST':
		subscribe=Newsletter.objects.create(email=request.POST.get('email'))
		subscribe.save()
	return render(request, 'mainapp/susbscribe.html',{'message':message})

	

def handler404(request, exception):
    return render(request, 'mainapp/404.html', status=404)

def handler500(request):
    return render(request, 'mainapp/500.html', status=500)

