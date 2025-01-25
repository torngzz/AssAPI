from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

#Id auto Increment ( created automatic)

class Customer(models.Model):    
    name = models.CharField(max_length=200, null=True) 
    phone = models.CharField(max_length=200, null=True)  
    email = models.CharField(max_length=200, null=True) 
    date_created = models.DateTimeField(auto_now_add=True, null=True) 

    def __str__(self):        
        return self.name 
    
class Category(models.Model):
    Categoryname=models.CharField(max_length=200,null=True)
    # CategoryImage=models.CharField(max_length=200,null=True)
    CategoryImage = models.ImageField(upload_to ='CategoryImages/')
    CategoryDate= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Categoryname

class Supplier(models.Model):    
    Companyname = models.CharField(max_length=200, null=True) 
    Contactname = models.CharField(max_length=200, null=True)
    ContactTitle = models.CharField(max_length=200, null=True)  
    phone = models.CharField(max_length=200, null=True)  
    email = models.CharField(max_length=200, null=True) 
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Companyname

class tblProducts(models.Model):
    productName = models.CharField(max_length=200, null=True)
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    SupplierID = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    quantity = models.CharField(max_length=200, null=True)
    priceIn = models.CharField(max_length=200, null=True)
    priceOut = models.CharField(max_length=200, null=True)
    instock = models.CharField(max_length=200, null=True) 
    rating = models.CharField(max_length=200, null=True) 
    description = models.CharField(max_length=200, null=True) 
    productImage = models.ImageField(upload_to ='ProductImages/')
    productDate = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):         
        return self.productName

class tblClients(models.Model):
    clientName = models.CharField(max_length=200, null=True)
    clientImage = models.ImageField(upload_to="pics")
    #clientDescription = RichTextField(null=True)
    clientDescription = RichTextUploadingField(null=True)
    def __str__(self):
        return self.clientName
    
class tblTopMenu(models.Model):
    topMenuName = models.CharField(max_length=200, null=True)
    topMenuImage = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.topMenuName

class tblSubTopMenu(models.Model):
    subTopMenuName = models.CharField(max_length=200, null=True)
    subTopMenuImage = models.CharField(max_length=200, null=True)
    TopMenuID = models.ForeignKey(tblTopMenu, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.subTopMenuName}'  

class tblSub2TopMenu(models.Model):
    sub2TopMenuName = models.CharField(max_length=200, null=True)
    sub2TopMenuImage = models.CharField(max_length=200, null=True) 
    subTopMenuID = models.ForeignKey(tblSubTopMenu, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.sub2TopMenuName}'  

class tblSocialMedia(models.Model):
    socialMediaName = models.CharField(max_length=200, null=True)
    socialMediaURL = models.CharField(max_length=200, null=True)
    socialMediaImage = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.socialMediaImage
    
class tblSlides(models.Model):
    slideName = models.CharField(max_length=200, null=True)
    slideImage = models.ImageField(upload_to ='images/',null=True)
    slideDescription = RichTextUploadingField(null=True)
    active = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.slideName}'
    
class tblProductDetail(models.Model):
    productDetailName = models.CharField(max_length=200, null=True)
    productDetailDate = models.DateTimeField (auto_now_add=True, null=True)
    productID = models.ForeignKey(tblProducts, on_delete=models.CASCADE, null=True)
    productSize =  RichTextUploadingField(null=True)
    productColor = RichTextUploadingField(null=True)

    def __str__(self):
        return f'{self.productDetailName}'

class tblProductDetailImage(models.Model):
    productDetailImageName = models.CharField(max_length=200, null=True)
    productID = models.ForeignKey(tblProducts, on_delete=models.CASCADE, null=True)
    productDetailImage = models.ImageField(upload_to='',null=True,blank=True)
    imageDate = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.productDetailImageName}'

class tblFooter(models.Model):
    footerName = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.footerName
    
class tblSubFooter(models.Model):
    footerID = models.ForeignKey(tblFooter, on_delete=models.CASCADE, null=True)
    subFooterName = models.CharField(max_length=200, null=True)
    subFooterURL = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.footerID} {self.footerID.footerName}'

