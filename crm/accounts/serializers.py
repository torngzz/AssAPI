from rest_framework import serializers

from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
      model = tblProducts
      fields = ['id', 'productName', 'priceOut','productImage','productDate']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:        
      model = Category
      fields = ['id', 'Categoryname', 'CategoryImage','CategoryDate']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:        
      model = tblClients
      fields = ['id', 'clientName', 'clientImage','clientDescription']

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:        
      model = tblSocialMedia
      fields = ['id', 'socialMediaName', 'socialMediaURL','socialMediaImage']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:        
      model = Customer
      fields = ['id', 'name', 'phone','email','date_created']

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:        
      model = Supplier
      fields = ['id', 'Companyname', 'Contactname','ContactTitle', 'phone','email','date_created']

class TopMenuSerializer(serializers.ModelSerializer):
    class Meta:        
      model = tblTopMenu
      fields = ['id', 'topMenuName', 'topMenuImage']

class SubTopMenuSerializer(serializers.ModelSerializer):
    class Meta:        
      model = tblSubTopMenu
      fields = ['id', 'subTopMenuName', 'subTopMenuImage','TopMenuID']

class Sub2TopMenuSerializer(serializers.ModelSerializer):
    class Meta:        
      model = tblSub2TopMenu
      fields = ['id', 'sub2TopMenuName', 'sub2TopMenuImage','subTopMenuID']

class SlideSerializer(serializers.ModelSerializer):
    class Meta:        
      model = tblSlides
      fields = ['id', 'slideName', 'slideImage', 'slideDescription', 'active']

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:        
      model = tblProductDetail
      fields = ['id', 'productDetailName', 'productDetailDate', 'productID', 'productSize', 'productColor']

class ProductDetailImageSerializer(serializers.ModelSerializer):
    class Meta:        
      model = tblProductDetailImage
      fields = ['id', 'productDetailImageName', 'productID', 'productDetailImage', 'imageDate']

class FooterSerializer(serializers.ModelSerializer):
    class Meta:        
      model = tblFooter
      fields = ['id', 'footerName']

class SubFooterSerializer(serializers.ModelSerializer):
    class Meta:        
      model = tblSubFooter
      fields = ['id', 'footerID', 'subFooterName','subFooterURL']