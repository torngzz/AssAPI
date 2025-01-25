from django.urls import path
from . import views
from .views import * 

urlpatterns = [
    # path('index/', views.home),
    path('', views.Index),
    path('productDetails/<int:pk>/', views.productDetails, name='productDetails'),
    path('about/', views.About, name='about'),
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
 
    path('Pros/', ProductListCreate.as_view(), name='ProList'),
    path('Pros/<int:pk>/', ProductDetail.as_view(), name='ProDetail'),
 
    path('Category/', CategoryListCreate.as_view(), name='CategoryList'),
    path('Category/<int:pk>/', CategoryDetail.as_view(), name='CategoryDetail'),
 
    path('Client/', ClientListCreate.as_view(), name='ClientList'),
    path('Client/<int:pk>/', ClientDetail.as_view(), name='ClientDetail'),
 
    path('SocialMedia/', SocialMediaListCreate.as_view(), name='SocialMediaList'),
    path('SocialMedia/<int:pk>/', SocialMediaDetail.as_view(), name='SocialMediaDetail'),
 
    path('Customers/', CustomerListCreate.as_view(), name='CustomerList'),
    path('Customers/<int:pk>/', CustomerDetail.as_view(), name='CustomerDetail'),
 
    path('Supplier/', SupplierListCreate.as_view(), name='CategoryList'),
    path('Supplier/<int:pk>/', SupplierDetail.as_view(), name='CategoryDetail'),
 
    path('TopMenu/', TopMenuListCreate.as_view(), name='TopMenuList'),
    path('TopMenu/<int:pk>/', TopMenuDetail.as_view(), name='TopMenuDetail'),
 
    path('SubTopMenu/', SubTopMenuListCreate.as_view(), name='SubTopMenuList'),
    path('SubTopMenu/<int:pk>/', SubTopMenuDetail.as_view(), name='SubTopMenuDetail'),
 
    path('Sub2TopMenu/', Sub2TopMenuListCreate.as_view(), name='Sub2TopMenuList'),
    path('Sub2TopMenu/<int:pk>/', Sub2TopMenuDetail.as_view(), name='Sub2TopMenuDetail'),
 
    path('Slide/', SlideListCreate.as_view(), name='SlideList'),
    path('Slide/<int:pk>/', SlideDetail.as_view(), name='SlideDetail'),
 
    path('ProductDetail/', ProductDetailListCreate.as_view(), name='ProductDetailList'),
    path('ProductDetail/<int:pk>/', ProductDetailDetail.as_view(), name='ProductDetailDetail'),
 
    path('ProductDetailImage/', ProductDetailImageListCreate.as_view(), name='ProductDetailImageList'),
    path('ProductDetailImage/<int:pk>/', ProductDetailImageDetail.as_view(), name='ProductDetailImageDetail'),
 
    path('Footer/', FooterListCreate.as_view(), name='FooterList'),
    path('Footer/<int:pk>/', FooterDetail.as_view(), name='FooterDetail'),
 
    path('SubFooter/', SubFooterListCreate.as_view(), name='SubFooterList'),
    path('SubFooter/<int:pk>/', SubFooterDetail.as_view(), name='SubFooterDetail'),
]