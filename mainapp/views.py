from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator 
from django.urls import reverse
from accounts.models import Profile, CustomUser as User
from .models import BookCategory, Department, ContactUs, Blog, Comment, Newsletter, Advert, ProductCategory, School, AdvertImages
from .forms  import CommentUpdateForm, AdvertForm
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
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
	slug=blog
	# blogs=blog.user
	# autor=Profile.objects.get(user=blogs)
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

	# def get_context_data(self, *args, **kwargs):
	# 	context=super().get_context_data(**kwargs)
	# 	context['school']=School.objects.all()
	# 	context['departments']=Department.objects.all()
	# 	return context
def filter_processing(request):
	if request.method=='GET':
		q=request.GET.get('q')
		print(q)
		if len(q)!=0:
			if q =='All':
				return redirect ('departments')
			school=School.objects.get(school_name=q)
			filter_result=school.department_set.all()
			print(filter_result)
			return render( request,'mainapp/departments.html', {'filter_result':filter_result})
	else:
		return redirect ('departments')

def bookdetailview(request, slug):
	book=BookCategory.objects.get(slug=slug)
	related=book.department
	related=BookCategory.objects.filter(department=related)
	print(related)
	return render (request, 'mainapp/bookdetailview.html', {'book':book, 'related':related})


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
		# send form message to email

		subject=request.POST.get('name')
		from_email=request.POST.get('email')
		message=request.POST.get('message')

		try:
			send_mail(subject, message, from_email, ["forscholarsedu@gmail.com"])
		except BadHeaderError:
			return HttpResponse('invalid header found.')

		# return redirect('subscribed')
		return render(request, 'mainapp/susbscribe.html')
	return render (request, 'mainapp/contact.html')


def search(request):
	# q=request.GET.get('q') if request.GET.get('q') !=None else ''
	if request.method== 'GET':
		q=request.GET.get('q') 
		if len(q)==0:
			return redirect('departments')

	# else:
		
	books=BookCategory.objects.filter(title__icontains=q)
	return render(request, 'mainapp/text_bk_detail.html', {'books':books})

def newsletter(request):
	message='susbscribed'
	if request.method=='POST':
		try:
			email=Newsletter.objects.get(email=request.POST.get('email'))
			return HttpResponse('Already a subscriber! Enter a different email')
		except:
			subscribe=Newsletter.objects.create(email=request.POST.get('email'))
			subscribe.save()
	return render(request, 'mainapp/susbscribe.html',{'message':message})

#advert view
class AdvertView(CreateView):
	form_class=AdvertForm
	model=Advert
	success_url='home'
	template_name='mainapp/advertform.html'

	def post(self,request, *args, **kwargs):
		form=AdvertForm(request.POST, request.FILES)
		user=request.user
		if form.is_valid():
			data=form.cleaned_data
			owner=form.save(commit=False)
			owner.user=user
			owner.save()
			images=request.FILES.getlist('images')
			if images:
				for  image in images:
					product_images=AdvertImages.objects.create(advert=owner, product_image=image)
					product_images.save()
			return redirect(self.success_url)
		return render (request, self.template_name)

def advert_list(request):
	advert=Advert.objects.all()
	paginator = Paginator(advert, 5) # Show 25 contacts per page.
	page_number = request.GET.get('page') 
	page_obj = paginator.get_page(page_number) 
	return render(request, 'mainapp/buy-items.html', {'advert':advert, 'paginator':paginator, 'page_number':page_number, 'page_obj':page_obj})

def advert_detail(request,pk):
	item=Advert.objects.get(pk=pk)
	user=item.user
	print(user)
	related=item.product_category
	images=item.advertimages_set.all()[:4]
	related=Advert.objects.filter(product_category=related)
	return render(request, 'mainapp/product-detail.html', {'item':item,'user':user, 'images':images, 'related':related})

def handler404(request, exception):
    return render(request, 'mainapp/404.html', status=404)

def handler500(request):
    return render(request, 'mainapp/500.html', status=500)

