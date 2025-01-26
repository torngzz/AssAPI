from django.urls import path
from . import views
from .views import * 

urlpatterns = [
    path('', views.Index),
    path('Home', views.Index),
    path('productDetails/<int:pk>/', views.productDetails, name='productDetails'),
    path('about/', views.About, name='about'),
    path('ConfirmPayment/', views.ConfirmPayment, name='ConfirmPayment'),
    path('Service/', views.Service, name='Service'),
    path('Portforlio/', views.Portforlio,name='Portforlio'),
    path('Pricing/', views.Pricing, name='Pricing'),
    path('Blog/', views.Blog, name='Blog'),
    path('Contact/', views.Contact, name='Contact'),
    path('Team/', views.Team, name='Team'),
    path('Testimonials/', views.Testimonials, name='Testimonials'),
    path('products/', views.products, name='products'),
    path('customer/', views.customer, name='customer'),
    path('contactUs/', views.contactUs, name='contactUs'),
    path('AboutUs/', views.AboutUs, name='AboutUs'),
    path('Search/',views.Search, name='Search'),
    path('Menu/',views.Menu, name='Menu'),
    path('GetValue/',views.GetValue, name='GetValue'),
    path('Categorys/',views.ListCategory, name='Categorys'),
    path('ShopingCart/',views.ProductCarts, name='ProductCarts'),
    path('addToCart/<int:product_id>/<int:quantity>/', views.add_to_cart, name='add_to_cart'),
    path('processPayment/', views.processPayment, name='processPayment'),
]