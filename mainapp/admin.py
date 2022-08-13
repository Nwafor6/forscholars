from django.contrib import admin
from .models import (BookCategory,Department, Blog, Comment, Newsletter, ProductCategory, Advert, School, ContactUs,AdvertImages )
# Register your models here.

class BookCategoryAdmin(admin.ModelAdmin):
	list_display=['title','department','file_type','semester','year','user','posted_on' ]
	prepopulated_fields ={'slug':('title',)}

admin.site.register(BookCategory,BookCategoryAdmin,)

class DeptAdmin(admin.ModelAdmin):
	list_display=['school','title','faculty']
	prepopulated_fields= {'slug': ('title',)}

admin.site.register(Department,DeptAdmin)

class BlogAdmin(admin.ModelAdmin):
	list_display=['title','date_posted', 'user']
	prepopulated_fields= {'slug': ('title',)}

class AdvertAdmin(admin.ModelAdmin):
	list_display=['product_name','product_category', 'product_price', 'status', 'product_quantity','clicks']
	prepopulated_fields= {'slug': ('product_name',)}

class SchoolAdmin(admin.ModelAdmin):
	prepopulated_fields= {'slug': ('school_name',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(ContactUs)
admin.site.register(Newsletter)
admin.site.register(ProductCategory)
admin.site.register(Advert, AdvertAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(AdvertImages)



