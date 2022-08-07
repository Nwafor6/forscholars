from django.contrib import admin
from .models import (BookCategory,Department, Blog, Comment, Newsletter)
# Register your models here.

class BookCategoryAdmin(admin.ModelAdmin):
	list_display=['title','department','file_type','semester','year','user','posted_on' ]
	prepopulated_fields ={'slug':('title',)}

admin.site.register(BookCategory,BookCategoryAdmin,)

class DeptAdmin(admin.ModelAdmin):
	list_display=['title','faculty']
	prepopulated_fields= {'slug': ('title',)}

admin.site.register(Department,DeptAdmin)

class BlogAdmin(admin.ModelAdmin):
	list_display=['title','date_posted', 'user']
	prepopulated_fields= {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(Newsletter)



