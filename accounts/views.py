from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import get_messages
from .models import CustomUser as User, Profile
from django.contrib.auth import authenticate, login, logout
from .forms import (CustomUserCreationForm,
	CustomUserChangeForm, ProfileUpdateForm )

# import for deactiavting user at first registraion
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token 
from django.core.mail import EmailMessage 
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMultiAlternatives
# end

# imports for password reset
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordResetForm
from django.db.models import Q
# end



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
		email_form=CustomUserChangeForm(instance=profile.user)
		if request.method == 'POST':
			form=ProfileUpdateForm(request.POST,request.FILES,instance=profile)
			email_form=CustomUserChangeForm(request.POST,instance=profile.user)
			if form.is_valid() & email_form.is_valid():
					form.save()
					email_form.save()
			return redirect('profile')
	return render(request, 'accounts/register_login.html', {'form':form, 'page':page, 'email_form':email_form})


def loginView(request):
	page='sign_in'
	if  request.method == "POST":
		email=request.POST.get('email')
		password=request.POST.get('password')
		redirect_to=request.POST.get('next')
		print(redirect_to,'.........')

		try:
			user = User.objects.get(email=email)
		except:
			messages.error(request, 'User does not exits')
		user= authenticate(request, email=email, password=password)
		if user is not None:
			login(request, user)
			try:
				return redirect(redirect_to)
			except:
				return redirect('home')
		else:
			messages.error(request, 'or username or password incorrect')
	return render(request, 'accounts/register_login.html', {'page':page} )	

def registrationView(request):
	page='reg'
	if request.method == "POST":
		form=CustomUserCreationForm(request.POST)
		# valuenext= request.POST.get('next')
		if form.is_valid():
			user=form.save(commit =False)
			user.is_active = False
			user.save()
			# login(request,user)
			# return redirect('home')

			try:
				# to get the domain of the current site 
				from_email='nwaforglory6@gmail.com'
				current_site = get_current_site(request) 
				mail_subject = 'Activation link has been sent to your email id'

				message = render_to_string('accounts/acc_active_email.html', {  
	                'user': user,  
	                'domain': current_site.domain,  
	                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
	                'token':account_activation_token.make_token(user),  
	            })

				to_email = form.cleaned_data.get('email')
				msg = EmailMultiAlternatives(mail_subject, message, from_email, [to_email]) 
				msg.attach_alternative(message, "text/html") 
				msg.send()  
				return render(request, 'accounts/reg_email_set_confirm.html')
			except:
				User.objects.all().first().delete()
	else:
		form=CustomUserCreationForm()	
	return render(request, 'accounts/register_login.html',{'form':form, 'page':page})



def logoutView_1(request):
	return render(request, 'accounts/register_login.html')

def logoutView(request):
	logout(request)
	return redirect('home')

# activation View
def activate(request, uidb64, token):  
    try:  
        uid = force_text(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return render(request, 'accounts/email_confirm_success.html') 
    else:  
        return HttpResponse('Activation link is invalid!')
# reset user pasword
def password_reset_request(request):
	if request.user.is_authenticated:
		return redirect('home')
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		current_site = get_current_site(request)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password/password_reset_email.html"
					c = {
					"email":user.email,
					'domain':current_site.domain,
					'site_name': 'Biriwka',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					message = render_to_string(email_template_name, c)
					try:
						# send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
						
						msg = EmailMultiAlternatives(subject, message, 'nwaforglory6@gmail.com', [user.email]) 
						msg.attach_alternative(message, "text/html") 
						msg.send() 
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("password_reset_done")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})
