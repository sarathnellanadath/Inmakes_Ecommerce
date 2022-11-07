from django.urls import path
from . import views
app_name = 'shop'

urlpatterns = [
    path('', views.allprdctct, name='allprdctct'),
    path('<slug:c_slug>/', views.allprdctct, name='products_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/', views.productdetail, name='productdetail'),
]