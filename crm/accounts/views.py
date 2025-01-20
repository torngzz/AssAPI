from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import *

from .models import *

# Create your views here.

# ListCreateAPIView provides GET (list) and POST (create) actions
class ProductListCreate(generics.ListCreateAPIView):
    queryset = tblProducts.objects.all()    
    serializer_class = ProductSerializer
# RetrieveUpdateDestroyAPIView provides GET (retrieve), PUT (update), DELETE (destroy) actions
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = tblProducts.objects.all()
    serializer_class = ProductSerializer

# ListCreateAPIView provides GET (list) and POST (create) actions
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()    
    serializer_class = CategorySerializer
# RetrieveUpdateDestroyAPIView provides GET (retrieve), PUT (update), DELETE (destroy) actions
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# ListCreateAPIView provides GET (list) and POST (create) actions
class ClientListCreate(generics.ListCreateAPIView):
    queryset = tblClients.objects.all()    
    serializer_class = ClientSerializer
# RetrieveUpdateDestroyAPIView provides GET (retrieve), PUT (update), DELETE (destroy) actions
class ClientDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = tblClients.objects.all()
    serializer_class = ClientSerializer

# ListCreateAPIView provides GET (list) and POST (create) actions
class SocialMediaListCreate(generics.ListCreateAPIView):
    queryset = tblSocialMedia.objects.all()    
    serializer_class = SocialMediaSerializer
# RetrieveUpdateDestroyAPIView provides GET (retrieve), PUT (update), DELETE (destroy) actions
class SocialMediaDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = tblSocialMedia.objects.all()
    serializer_class = SocialMediaSerializer

# ListCreateAPIView provides GET (list) and POST (create) actions
class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()    
    serializer_class = CustomerSerializer
# RetrieveUpdateDestroyAPIView provides GET (retrieve), PUT (update), DELETE (destroy) actions
class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# ListCreateAPIView provides GET (list) and POST (create) actions
class SupplierListCreate(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()    
    serializer_class = SupplierSerializer
# RetrieveUpdateDestroyAPIView provides GET (retrieve), PUT (update), DELETE (destroy) actions
class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

# ListCreateAPIView provides GET (list) and POST (create) actions
class TopMenuListCreate(generics.ListCreateAPIView):
    queryset = tblTopMenu.objects.all()    
    serializer_class = TopMenuSerializer
# RetrieveUpdateDestroyAPIView provides GET (retrieve), PUT (update), DELETE (destroy) actions
class TopMenuDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = tblTopMenu.objects.all()
    serializer_class = TopMenuSerializer

# ListCreateAPIView provides GET (list) and POST (create) actions
class SubTopMenuListCreate(generics.ListCreateAPIView):
    queryset = tblSubTopMenu.objects.all()    
    serializer_class = SubTopMenuSerializer
# RetrieveUpdateDestroyAPIView provides GET (retrieve), PUT (update), DELETE (destroy) actions
class SubTopMenuDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = tblSubTopMenu.objects.all()
    serializer_class = SubTopMenuSerializer

# ListCreateAPIView provides GET (list) and POST (create) actions
class Sub2TopMenuListCreate(generics.ListCreateAPIView):
    queryset = tblSub2TopMenu.objects.all()    
    serializer_class = Sub2TopMenuSerializer
# RetrieveUpdateDestroyAPIView provides GET (retrieve), PUT (update), DELETE (destroy) actions
class Sub2TopMenuDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = tblSub2TopMenu.objects.all()
    serializer_class = Sub2TopMenuSerializer

# ListCreateAPIView provides GET (list) and POST (create) actions
class SlideListCreate(generics.ListCreateAPIView):
    queryset = tblSlides.objects.all()    
    serializer_class = SlideSerializer
# RetrieveUpdateDestroyAPIView provides GET (retrieve), PUT (update), DELETE (destroy) actions
class SlideDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = tblSlides.objects.all()
    serializer_class = SlideSerializer

# ListCreateAPIView provides GET (list) and POST (create) actions
class ProductDetailListCreate(generics.ListCreateAPIView):
    queryset = tblProductDetail.objects.all()    
    serializer_class = ProductDetailSerializer
# RetrieveUpdateDestroyAPIView provides GET (retrieve), PUT (update), DELETE (destroy) actions
class ProductDetailDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = tblProductDetail.objects.all()
    serializer_class = ProductDetailSerializer

# ListCreateAPIView provides GET (list) and POST (create) actions
class ProductDetailImageListCreate(generics.ListCreateAPIView):
    queryset = tblProductDetailImage.objects.all()    
    serializer_class = ProductDetailImageSerializer
# RetrieveUpdateDestroyAPIView provides GET (retrieve), PUT (update), DELETE (destroy) actions
class ProductDetailImageDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = tblProductDetailImage.objects.all()
    serializer_class = ProductDetailImageSerializer

# ListCreateAPIView provides GET (list) and POST (create) actions
class FooterListCreate(generics.ListCreateAPIView):
    queryset = tblFooter.objects.all()    
    serializer_class = FooterSerializer
# RetrieveUpdateDestroyAPIView provides GET (retrieve), PUT (update), DELETE (destroy) actions
class FooterDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = tblFooter.objects.all()
    serializer_class = FooterSerializer

# ListCreateAPIView provides GET (list) and POST (create) actions
class SubFooterListCreate(generics.ListCreateAPIView):
    queryset = tblSubFooter.objects.all()    
    serializer_class = SubFooterSerializer
# RetrieveUpdateDestroyAPIView provides GET (retrieve), PUT (update), DELETE (destroy) actions
class SubFooterDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = tblSubFooter.objects.all()
    serializer_class = SubFooterSerializer

def Index(request):
    Products = tblProducts.objects.all()
    Categorys = Category.objects.all()
    TopMenu = tblTopMenu.objects.all()
    SubTopMenu = tblSubTopMenu.objects.all()
    
    context = {
        'Products' : Products,
        'Categories' : Categorys,
        'SubTopMenus' : SubTopMenu,
        'TopMenus' : TopMenu
    }
    return render(request, 'accounts/index.html', context)

def productDetails(request, pk):
    Product = tblProducts.objects.get(id = pk)
    context = {
        'Products' : Product
    }
    # context = {
    #     'Products' = Product
    # }
    return render(request,'accounts/productDetails.html', context)

def About(request):
    return render(request,'accounts/about.html')

def Service(request):
    return render(request,'accounts/services.html')

def Portforlio(request):
    return render(request,'accounts/portfolio.html')

def Pricing(request):
    return render(request,'accounts/pricing.html')

def Blog(request):
    return render(request,'accounts/blog.html')

def Contact(request):
    return render(request,'accounts/contact.html')

def Team(request):
    return render(request,'accounts/team.html')

def Testimonials(request):
    return render(request,'accounts/testimonials.html')

def Single_Blog(request):
    return render(request,'accounts/blog-single.html')

def home(request):
    # return HttpResponse('Home_page')
    return render(request,'accounts/AboutUs.html')

def products(request):
    return HttpResponse('Products_page')

def customer(request):
    return HttpResponse('Customer_page')

def contactUs(request):
    return render(request, 'accounts/contactUs.html')

def AboutUs(request):
    return HttpResponse('This is my frist day of leaning python.')

def Search(request):
    return HttpResponse("If you have something ,search here....")
def Menu(request):
    return render(request,'accounts/menu.html')
def GetValue(request):
    
    #Caculate Total Price
    UnitPrice=1500
    Quantity=5
    TotalPrice=UnitPrice*Quantity

    #Find day

    Day=1
    Result=''
    if( Day==1):
        Result='The day is Monday'
    
    elif(Day==2):
        Result='The day is Tuesday'
    
    elif(Day==3):
        Result='The day is Wednesday'
    
    elif(Day==4):
        Result='The day is Thursday'
    
    elif(Day==5):
        Result="The day is Friday"
    
    elif(Day==6):
        Result='The day is Saturday'

    elif(Day==7):
        Result='The day is Sunday'
    
    context={
            'Products':'Hi Product',
            'TP':TotalPrice,
            'Day':Result,
            'DisplayDay':['Monday','Tuesday','Wednesday','Friday','Saturday','Sunday'],
            'DisplayMonth':['January','February','March','April','May','June','July','August','September','October','November','December']

    }
    return render(request,'accounts/GetValue.html',context)


def ListCategory(request):
    category = Category.objects.all()
    client = tblClients.objects.all()
    context = {
        'categorys' :category,
        'clients' :client,
    }
    return render(request, 'accounts/ListCategory.html', context)

    
