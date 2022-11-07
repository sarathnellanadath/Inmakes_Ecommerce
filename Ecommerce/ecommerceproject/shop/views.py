from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import category, product
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models.query import Q


# Create your views here.

def allprdctct(request, c_slug=None):
    c_page = None
    Products_list = None
    if c_slug != None:
        c_page = get_object_or_404(category, slug=c_slug)
        Products_list = product.objects.all().filter(category=c_page, available=True)
    else:
        Products_list = product.objects.all().filter(available=True)
    pageinator = Paginator(Products_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        Products = pageinator.page(page)
    except (EmptyPage, InvalidPage):
        Products = pageinator.page(pageinator.num_pages)

    img = category.objects.all()

    return render(request, 'category.html', {'category': c_page, 'products': Products,'img':img})


def productdetail(request, c_slug, p_slug):

    try:
        Product = product.objects.get(category__slug=c_slug, slug=p_slug)

    except Exception as e:
        raise e


    return render(request, 'product.html', {'product': Product})


