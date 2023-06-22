from django.shortcuts import render
from searchapp.models import Dish

def search_dish(request):
    query = request.GET.get('query')
    if query:
        results = Dish.objects.filter(name__contains=query)
    else:
        results = None

    return render(request, 'search.html', {'results': results})
