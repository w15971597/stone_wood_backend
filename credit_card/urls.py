from django.urls import path

from . import views


urlpatterns = [
	path('login', views.login, name='index'),
	path('home', views.home, name='index'),
	path('message', views.message, name='index'),

	path('card/create', views.create_card, name='index'),
	path('card/update', views.update_card, name='index'),
	path('card/search', views.search_card, name='index'),
	path('card/detail', views.get_card_detail, name='index'),

	path('bill/search', views.search_bill, name='index'),
	path('feedback', views.feedback, name='index'),
	path('operate', views.operate, name='index'),
	path('', views.index, name='index'),
]




