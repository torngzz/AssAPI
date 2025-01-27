from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework import generics
from .serializers import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm # type: ignore

from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import tblProducts, tblProductCarts
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
def About(request):
    return render(request,'accounts/about.html')

def Service(request):
    return render(request,'accounts/services.html')

def Portforlio(request):
    return render(request,'accounts/portfolio.html')

def Pricing(request):
    return render(request,'accounts/pricing.html')

def Blog(request):
    Products = tblProducts.objects.all()
    Categorys = Category.objects.all()
    TopMenu = tblTopMenu.objects.all()
    SubTopMenu = tblSubTopMenu.objects.all()

    userId = request.user.id

    totalCarts = tblProductCarts.objects.filter(UserId = userId).count();
    
    context = {
        'Products' : Products,
        'totalCarts' : totalCarts,
        'Categories' : Categorys,
        'SubTopMenus' : SubTopMenu,
        'TopMenus' : TopMenu,
        "userId" : userId
    }

    return render(request,'accounts/blog.html', context)

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


# -----------------------------------------------

def Index(request):
    Products = tblProducts.objects.all()
    Categorys = Category.objects.all()
    TopMenu = tblTopMenu.objects.all()
    SubTopMenu = tblSubTopMenu.objects.all()

    userId = request.user.id

    totalCarts = tblProductCarts.objects.filter(UserId = userId).count();
    
    context = {
        'Products' : Products,
        'totalCarts' : totalCarts,
        'Categories' : Categorys,
        'SubTopMenus' : SubTopMenu,
        'TopMenus' : TopMenu,
        "userId" : userId
    }
    return render(request, 'accounts/index.html', context)


def productDetails(request, pk):
    # Get the product based on the provided id (primary key)
    Product = tblProducts.objects.get(id=pk)
    
    # Ensure the rating is treated as an integer
    try:
        rating = int(Product.rating)  # Convert rating to an integer
    except ValueError:
        rating = 0  # If the rating is not a valid integer, default to 0
    
    # Get related products based on the category, excluding the current product
    RelatedProducts = tblProducts.objects.filter(categoryID=Product.categoryID).exclude(id=pk)
    
    # Get all top and sub top menus
    TopMenu = tblTopMenu.objects.all()
    SubTopMenu = tblSubTopMenu.objects.all()
    
    # Generate the rating range based on the product's rating
    rating_range = range(rating)  # This creates a range from 0 to rating-1
    userId = request.user.id
    
    totalCarts = tblProductCarts.objects.filter(UserId = userId).count()
    
    context = {
        'totalCarts' : totalCarts,
        'Products': Product,
        'RelatedProducts': RelatedProducts,
        'SubTopMenus': SubTopMenu,
        'TopMenus': TopMenu,
        'rating_range': rating_range  # Add this line to pass the range to the template
    }
    
    return render(request, 'accounts/productDetails.html', context)


@login_required
def ProductCarts(request):
    userId = request.user.id
    TopMenu = tblTopMenu.objects.all()
    SubTopMenu = tblSubTopMenu.objects.all()
    ProductCarts = tblProductCarts.objects.filter(UserId = userId).all()

    totalCarts = ProductCarts.count()
    
    totalPrice = sum(float(product.priceOut) * int(product.quantity) for product in ProductCarts)    # Get all top and sub top menus
    context = {
        'totalCarts' : totalCarts,
        'ProductCarts' :ProductCarts,
        'totalPrice' :totalPrice,
        'SubTopMenus': SubTopMenu,
        'TopMenus': TopMenu,
    }
    return render(request, 'accounts/shopingCart.html', context)

@login_required
def ConfirmPayment(request):
    userId = request.user.id
    ProductCarts = tblProductCarts.objects.filter(UserId = userId).all()
    totalPrice = sum(float(product.priceOut) * int(product.quantity) for product in ProductCarts)    # Get all top and sub top menus
    TopMenu = tblTopMenu.objects.all()
    SubTopMenu = tblSubTopMenu.objects.all()

    for product in ProductCarts: 
        product.priceOut = float(product.priceOut) * int(product.quantity);
    
    totalCarts = ProductCarts.count()
    
    context = {
        'totalCarts' : totalCarts,
        'ProductCarts' :ProductCarts,
        'totalPrice' :totalPrice,
        'SubTopMenus': SubTopMenu,
        'TopMenus': TopMenu,
    }
    return render(request, 'accounts/confirmPayment.html', context)


@login_required
def add_to_cart(request, product_id, quantity):
    # Ensure quantity is valid
    try:
        quantity = int(quantity)
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
    except (ValueError, TypeError):
        raise Http404("Invalid quantity")

    # Retrieve the product based on the product_id
    try:
        product = tblProducts.objects.get(id=product_id)
    except tblProducts.DoesNotExist:
        raise Http404("Product not found")

    userId = request.user.id
    # Insert product into tblProductCarts
    cart_item, created = tblProductCarts.objects.get_or_create(
        productId = product,
        UserId = userId,
        defaults={
            'quantity': quantity,
            'priceOut': product.priceOut,
            'productImage': product.productImage,
            'productName': product.productName
        }
    )

    if not created:  # If the cart item already exists, increase the quantity
        cart_item.quantity = quantity + int(cart_item.quantity);
        cart_item.save()

    totalCarts = tblProductCarts.objects.filter(UserId = userId).count();

    return JsonResponse({'status': 'success', 'message': f'{product.productName} added to cart!', "totalCarts": totalCarts})

@login_required
def processPayment(request):
    if request.method == 'POST':
        username = request.POST.get('first_name') + request.POST.get('last_name')
        country = request.POST.get('country')
        address = request.POST.get('address')
        bank_account = request.POST.get('bank_account')
        amount = request.POST.get('totalAmount')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        remark = request.POST.get('remark')
        userId = request.user.id

        transaction = tblTransactions(
            UserId = userId,
            Username=username,
            Country=country,
            Address=address,
            BankAccount=bank_account,
            Amount=amount,
            Phone=phone,
            Email=email,
            Remark=remark
        )
        transaction.save()

        tblProductCarts.objects.filter(UserId = userId).delete()
        
        return HttpResponseRedirect('/Home')  # Redirect to a success page after processing the order

    return render(request, 'index.html')


# Registration view
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)  # Log the user in after registration
            return HttpResponseRedirect('/Home') # Redirect to homepage or wherever you want
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect('/Home') # Redirect to the homepage or dashboard
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def Shop(request):
    # Fetch all necessary objects
    Products = tblProducts.objects.all()
    Categories = Category.objects.all()
    TopMenu = tblTopMenu.objects.all()
    SubTopMenu = tblSubTopMenu.objects.all()

    # Handle category filtering
    selected_category = request.GET.get('category')
    if selected_category:
        Products = Products.filter(categoryID=selected_category)

    totalCarts = tblProducts.objects.count()  # Adjust this as per your cart logic

    context = {
        'Products': Products,
        'Categories': Categories,
        'SubTopMenus': SubTopMenu,
        'TopMenus': TopMenu,
        'totalCarts': totalCarts,
    }
    return render(request, 'accounts/shop-grid.html', context)
