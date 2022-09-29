from .models import Advert, Blog, School, Category
import random

# checking if there exits any in the database
# ads=int(Advert.objects.all().count())
# x_read=int(Blog.objects.all().count())
# print(type(ads))

def category_context(request):
	
	categories=Category.objects.all()
	school=School.objects.all()

	return({'categories':categories, 'school':school})


def ads(request):
	pks =Advert.objects.filter(status='verified')
	pks=[i.pk for i in pks if len(pks)]
	# categories=Category.objects.all()
	# # for homepage
	# blogs=Blog.objects.all()
	# # for school filtering query
	# school=School.objects.all()
	# # for read_also
	# x_read=Blog.objects.all()
	# x_read=[i.slug for i in x_read]
	if len(pks) !=0:
		ads=random.choice(pks)
		return{'x_advert':Advert.objects.get(pk=ads)}
	# 	read_more=random.choice(x_read)
	# return{'x_advert':Advert.objects.get(pk=ads),'read_more':Blog.objects.get(slug=read_more), 'blogs':blogs, 'school':school}
	
	return ''

	
