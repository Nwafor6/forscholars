from  django import forms
from .models import Comment, Advert, AdvertImages


class CommentUpdateForm(forms.ModelForm):
	message = forms.CharField(widget= forms.Textarea(attrs={"placeholder":"Message......."}), max_length = 800)
	class Meta:
		model=Comment
		fields=['message']

class AdvertForm(forms.ModelForm):
	# images=forms.ImageField(widget=forms.FileInput(attrs={"multiple":"True",}),required=False, label='Product images', help_text='You can upload multile images')
	class Meta:
		model=Advert
		fields=['product_name','product_category','product_price','product_cover_image','description','product_quantity','product_location']


class PaidAdvertForm(forms.ModelForm):
	images=forms.ImageField(widget=forms.FileInput(attrs={"multiple":"True",}),required=False, label='Product images', help_text='You can upload multile images')
	class Meta:
		model=Advert
		fields=['product_name','product_category','product_price','product_cover_image','description','product_quantity','product_location']

