from django.urls import path
from . import views
# app_name='mainapp'
urlpatterns =[
	path('', views.home, name="home"),
	path('about', views.about, name="about"),
	path('category/<str:pk>/', views.categoryView, name="category"),
	path('blog', views.blog, name="blog"),
	path('blog/<slug:slug>/', views.blog_detail, name="_blog"),
	path('category', views.category, name="category"),
	path('contact', views.contact, name="contact"),

	# Books
	path('share/books/', views.ShareBookView.as_view(), name="share-books"),
	path('share/books/update/<str:pk>/', views.UpdateShareBookView.as_view(), name="share-books-update"),
	path('departments', views.DepartmentView.as_view(), name="departments"),
	path('filter-result', views.filter_processing, name="filter-result"),
	# path('department/<slug:slug>/', views.DepartmentContentView.as_view(), name="department"),
	path('past-questions/<str:pk>/', views.dept_PQ_detail, name="past-questions"),
	path('text-books/<str:pk>/', views.dept_TB_detail, name="text-books"),
	path('books/<str:pk>/', views.bookdetailview, name="books"),
	path('hand-outs/<str:pk>/', views.dept_HO_detail, name="hand-outs"),
	path('years', views.years, name="years"),
	path('search-books/', views.search, name="search-books"),
	path('subscribed/', views.newsletter, name="subscribed"),
	path('update-comment/<str:pk>/', views.update_comment, name='update-comment'),
	path('delete-comment/<str:pk>/', views.delete_comment, name='delete-comment'),

	# market view
	path('market-place/sell', views.AdvertView.as_view(), name='advertise'),
	path('market-place/item/update/<str:pk>/', views.AdvertUpdateView.as_view(), name='update-advertise'),
	path('buy-and-sell/', views.advert_list, name='buy-and-sell'),
	path('buy-and-sell/<str:pk>', views.advert_detail, name='item-detail'),

	# paid advert
	path('my-product/advertise', views.PaidAdvertView.as_view(), name='paid-advert'),

	# terms and condiction
	path('terms&conditions/', views.terms_condiction, name='terms&conditions'),
	path('privacy&policy', views.privacy, name='privacy&policy'),
	
]