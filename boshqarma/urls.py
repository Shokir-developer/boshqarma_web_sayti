from django.urls import path
from .views import index, news

urlpatterns = [
	path('', index, name='index'),
	path('news/', news, name='news'),
]
