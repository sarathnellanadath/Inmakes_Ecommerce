from django.shortcuts import render
from django.db.models.query import Q
from shop.models import product


def search_results(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
    return render(request, 'search.html', {'query': query, 'products': products})
