from  django import forms
from .models import Comment, Advert, AdvertImages, BookCategory, School, 	Department


class CommentUpdateForm(forms.ModelForm):
	message = forms.CharField(widget= forms.Textarea(attrs={"placeholder":"Message......."}), max_length = 800)
	class Meta:
		model=Comment
		fields=['message']

class AdvertForm(forms.ModelForm):
	# images=forms.ImageField(widget=forms.FileInput(attrs={"multiple":"True",}),required=False, label='Product images', help_text='You can upload multile images')
	class Meta:
		model=Advert
		fields=['product_name','product_category','product_price','product_cover_image','description','product_quantity','product_location','contact']


class PaidAdvertForm(forms.ModelForm):
	images=forms.ImageField(widget=forms.FileInput(attrs={"multiple":"True",}),required=False, label='Product images', help_text='You can upload multile images')
	class Meta:
		model=Advert
		fields=['product_name','product_category','product_price','product_cover_image','description','product_quantity','product_location','contact']

class ShareBookForm(forms.ModelForm):
	school=forms.ModelChoiceField(
        queryset=School.objects.all(),
        required=True,
        label="",
        help_text="Select you institution"

    )
	department=title= forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Chemistry"}),required=True, max_length = 100, label="", help_text="Department.")
	faculty = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Health sciences."}),required=True, max_length = 100, label="",help_text="Departments's Faculty")
	title= forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Basic Chemistry"}),required=True, max_length = 100, label="", help_text="Book Title.")
	course_code= forms.CharField(widget= forms.TextInput(attrs={"placeholder":"e.g: MAG 111."}),required=True, label="",help_text="Course Code")

	class Meta:
		model=BookCategory
		fields=['school','faculty','title','course_code','file','file_type','cover_img','semester','year']

	def __init__(self, *args, **kwargs):
		super(ShareBookForm, self).__init__(*args,**kwargs)

		for fieldname in ['file']:
			self.fields[fieldname].help_text="Paste file url. e.g: <span class='text-danger'>https://docs.google.com/document/d/14yyw-7C</span>"
			self.fields[fieldname].label=""

		for fieldname in ['semester','year','file_type','cover_img']:
			self.fields[fieldname].label=""

		for fieldname in ['year']:
			self.fields[fieldname].label=""
			self.fields[fieldname].help_text="Select Year"

		for fieldname in ['semester']:
			self.fields[fieldname].label=""
			self.fields[fieldname].help_text="Select Semester"

		for fieldname in ['file_type']:
			self.fields[fieldname].label=""
			self.fields[fieldname].help_text="Selet filetype"
			


        