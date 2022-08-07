from django.db import models
from django.template.defaultfilters import slugify
from accounts.models import CustomUser
from django.conf import settings

# Create your models here.
year_category=[
	('Year-1', 'Year-1'),
	('Year-2', 'Year-2'),
	('Year-3', 'Year-3'),
	('Year-4', 'Year-4')
]
semester_category=[
	('First', 'First'),
	('Second', 'Second'),
]
type_category=[
	('Texts Books', 'Texts Books'),
	('Past Questions', 'Past Questions'),
	('Hand Outs', 'Hand Outs'),
]
faculty_category=[
	('Physical Sciences', 'Physical Sciences'),
	('Bio Sciences', 'Bio Sciences'),
]
class Department(models.Model):
	title=models.CharField(max_length=200)
	cover_img=models.ImageField(blank=True, null=True)
	faculty=models.CharField(max_length=20, choices=faculty_category)
	slug=models.SlugField()

	class Meta:
		verbose_name_plural=('Departments')

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.title:
			self.slug=slugify(self.title)
		super(Department, self).save(*args,**kwargs)

class BookCategory(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
	department=models.ForeignKey(Department, on_delete=models.CASCADE)
	title=models.CharField(max_length=200)
	course_code=models.CharField(max_length=50, blank=True, null=True)
	about_book=models.CharField(max_length=200, blank=True, null=True)
	slug=models.SlugField()
	file=models.FileField()
	file_type=models.CharField(max_length=20, choices=type_category)
	cover_img=models.ImageField(blank=True, null=True)
	semester=models.CharField(max_length=20, choices=semester_category)
	year=models.CharField(max_length=20, choices=year_category)
	posted_on=models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name_plural=('BookCategories')

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.title:
			self.slug=slugify(self.title)
		super(BookCategory, self).save(*args,**kwargs)


class ContactUs(models.Model):

	name=models.CharField(max_length=50)
	email=models.EmailField()
	phone_no=models.CharField(max_length=50)
	message=models.TextField()

	def __str__(self):
		return self.name

class Blog(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
	title=models.CharField(max_length=100)
	slug=models.SlugField()
	body=models.TextField()
	blog_img=models.ImageField(blank=True, null=True)
	file=models.FileField(blank=True, null=True)
	date_posted=models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering=('-date_posted',)
	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug=slugify(self.title)
		super(Blog, self).save(*args,**kwargs)

class Comment(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
	blog=models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True, blank=True)
	message=models.CharField(max_length=400)
	slug=models.SlugField()
	date_posted=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.message

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug=slugify(self.message)
		super(Comment, self).save(*args,**kwargs)

class Newsletter(models.Model):
	email=models.EmailField()

	def __str__(self):
		return self.email


