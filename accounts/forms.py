from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

from django.contrib.auth.forms import UserChangeForm, UserCreationForm

# def __init__(self, *args, **kwargs):
#             super(LearnerSignUpForm, self).__init__(*args, **kwargs)

#             for fieldname in ['username', 'password1', 'password2']:
#                 self.fields[fieldname].help_text = None  


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ["email", 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args,**kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text=None

        for f in ['password2']:
            self.fields[f].label='Confirm Password'




class CustomUserChangeForm(UserChangeForm):
    email= forms.EmailField(max_length = 50 ,widget=forms.TextInput(attrs={'placeholder':'@example.com'}))
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        ## remove label from each of the fields
        for f in self.fields.keys():
            self.fields[f].help_text=''
    class Meta:
        model = CustomUser
        fields = ["email"]

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=["profile_img", "department", "phone","bio"]