from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["email"]


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
		fields=["profile_img", "first_name", "last_name", "department", "phone","bio"]