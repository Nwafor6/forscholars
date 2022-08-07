from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import CustomUser as User, Profile
from django.contrib.auth import authenticate, login, logout
from .forms import (CustomUserCreationForm,
	CustomUserChangeForm, ProfileUpdateForm )



# Create your views here.

def profile(request):
	if 	request.user.is_authenticated:
		profile =Profile.objects.get(user=request.user)
	context={'profile':profile}
	return render(request, 'accounts/profile.html',context)

def profileUpdate(request):
	page= 'profile'
	if request.user.is_authenticated:
		profile =Profile.objects.get(user=request.user)
		form=ProfileUpdateForm(instance=profile)
		if request.method == 'POST':
			form=ProfileUpdateForm(request.POST,request.FILES,instance=profile)
			if form.is_valid():
					form.save()
			return redirect('profile')
	return render(request, 'accounts/register_login.html', {'form':form, 'page':page})



def loginView(request):
	page='sign_in'
	if  request.method == "POST":
		email=request.POST.get('email')
		password=request.POST.get('password')

		try:
			user = User.objects.get(email=email)
		except:
			return HttpResponse('Incorrect Uername or password')
		user= authenticate(request, email=email, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			return HttpResponse('error')
	return render(request, 'accounts/register_login.html', {'page':page})	

def registrationView(request):
	page='reg'
	if request.method == "POST":
		form=CustomUserCreationForm(request.POST)
		if form.is_valid():
			user=form.save()
			login(request,user)
			return redirect('home')
	else:
		form=CustomUserCreationForm()	
	return render(request, 'accounts/register_login.html',{'form':form, 'page':page})



def logoutView_1(request):
	return render(request, 'accounts/register_login.html')

def logoutView(request):
	logout(request)
	return redirect('home')

