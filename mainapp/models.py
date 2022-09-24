from django.db import models
from django.template.defaultfilters import slugify
from accounts.models import CustomUser
from django.conf import settings

# Create your models here.
year_category=[
	('Year-1', 'Year-1'),
	('Year-2', 'Year-2'),
	('Year-3', 'Year-3'),
	('Year-4', 'Year-4'),
	('Year-5', 'Year-5'),
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

class School(models.Model):
	school_name=models.CharField(max_length=200, unique=True)
	slug=models.SlugField()
	logo=models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.school_name

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug=slugify(self.school_name)
		super(School, self).save(*args,**kwargs)



class Department(models.Model):
	school=models.ForeignKey(School, models.SET_NULL, null=True, blank=True)
	title=models.CharField(max_length=200)
	cover_img=models.ImageField(blank=True, null=True)
	faculty=models.CharField(max_length=50)
	slug=models.SlugField()

	class Meta:
		verbose_name_plural=('Departments')

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
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
		if not self.slug:
			self.slug=slugify(self.title+self.id)
		super(BookCategory, self).save(*args,**kwargs)


class ContactUs(models.Model):

	name=models.CharField(max_length=50)
	email=models.EmailField()
	phone_no=models.CharField(max_length=50)
	message=models.TextField()

	def __str__(self):
		return self.name

class Category(models.Model):
	title=models.CharField(max_length=200)

	def __str__(self):
		return self.title

class Blog(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
	title=models.CharField(max_length=100)
	slug=models.SlugField()
	body=models.TextField()
	blog_img=models.ImageField(blank=True, null=True)
	file=models.FileField(blank=True, null=True)
	Category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
	date_posted=models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering=('-date_posted',)
	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug=slugify(self.title)
		super(Blog, self).save(*args,**kwargs)


class BlogImages(models.Model):
	blog=models.ForeignKey(Blog, on_delete=models.CASCADE)
	image=models.ImageField()

	def __str__(self):
		return self.blog.title

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


# adverts 
class ProductCategory(models.Model):
	title=models.CharField(max_length=50)

	class Meta:
		verbose_name_plural=('Product Categories')

	def __str__(self):
		return self.title
STATUS=[
	('verified','verified'),
	('pending','pending'),
	('rejected','rejected'),
]

class Advert(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	product_category=models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
	product_name=models.CharField(max_length=50)
	slug=models.SlugField(blank=True, null=True)
	product_price=models.PositiveIntegerField()
	product_cover_image=models.ImageField(upload_to='product-images')
	description=models.CharField(max_length=300)
	status=models.CharField(max_length=50, choices=STATUS, default='pending')
	product_quantity=models.PositiveIntegerField()
	product_location=models.CharField(max_length=100)
	contact=models.CharField(max_length=60, null=True,blank=True)
	posted_on=models.DateTimeField(auto_now_add=True)
	clicks=models.IntegerField(default=0)

	def __str__(self):
		return self.product_name

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug=slugify(self.product_name)
		super(Advert, self).save(*args,**kwargs)

	@property
	def images(self):
		"""return all list of all uploaded images"""
		return self.avertimages_set.all() 

class AdvertImages(models.Model):
	product_image=models.ImageField(null=True, blank=True, upload_to='product-images')
	advert=models.ForeignKey(Advert, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.advert.product_name} images"


		