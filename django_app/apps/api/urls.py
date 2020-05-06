from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'books', views.BookViewset, 'book')
router.register(r'authors', views.AuthorViewset, 'author')
router.register(r'subscribers', views.SubscriberViewset, 'subscriber')
router.register(r'languages', views.LanguagesViewset, 'language')
router.register(r'search', views.SearchViewset, 'search')


urls = [
    path('', include(router.urls)),
]
