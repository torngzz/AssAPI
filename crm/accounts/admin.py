from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.

admin.site.site_header = "ACLEDA University of Business"
admin.site.site_title = "ACLEDA University of Business Admin Panel"
admin.site.index_title = " Admin Panel"


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","productName","image_preview","categoryID","SupplierID","priceIn","productDate"]
    list_filter = ["productDate"]
    search_fields = ["productName"]
    date_hierarchy = "productDate" 
    readonly_fields = ["image_preview"]
    

    def image_preview(self, obj):
        if obj.productImage:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.productImage.url)
        return "No Image"

    image_preview.short_description = 'Image Preview'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","Categoryname","image_preview","CategoryDate"]
    list_filter = ["Categoryname","CategoryDate"]
    search_fields = ["Categoryname"]
    readonly_fields = ["image_preview"]

    
    def image_preview(self, obj):
        if obj.CategoryImage:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.CategoryImage.url)
        return "No Image"

    image_preview.short_description = 'Image Preview'

class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id","name","phone","email","date_created"] 
    list_filter = ["date_created"]
    search_fields = ["name"]
    date_hierarchy = "date_created"

class SupplierAdmin(admin.ModelAdmin):
    list_display = ["id","Companyname","Contactname","ContactTitle","phone","email","date_created"]
    list_filter = ["date_created"]
    search_fields = ["Companyname"]
    date_hierarchy = "date_created"

# class SlideAdmin(admin.ModelAdmin):
#     list_display = ["id","slideName","image_preview"]
#     list_filter = ["slideName"]
#     search_fields = ["slideName"]   

    
#     def image_preview(self, obj):
#         if obj.slideImage:
#             return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.CategoryImage.url)
#         return "No Image"

#     image_preview.short_description = 'Image Preview'

admin.site.register(Category, CategoryAdmin)
admin.site.register(tblProducts, ProductAdmin)
admin.site.register(tblTopMenu)
admin.site.register(tblSubTopMenu)
admin.site.register(tblProductDetail)
admin.site.register(tblProductCarts)
admin.site.register(tblTransactions)
admin.site.register(tblProductDiscount)
# admin.site.register(tblSub2TopMenu)

# admin.site.register(Customer, CustomerAdmin)
# admin.site.register(Supplier, SupplierAdmin)
# admin.site.register(tblClients)
# admin.site.register(tblSocialMedia)
# admin.site.register(tblSlides)
# admin.site.register(tblProductDetailImage)
# admin.site.register(tblFooter)
# admin.site.register(tblSubFooter)