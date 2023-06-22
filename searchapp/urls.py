from django.urls import path
from searchapp.views import search_dish

urlpatterns = [
    path('search/', search_dish, name='search-dish'),
]
