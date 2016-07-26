# Systeme
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os

# Applications
from storeMagento.models import *

# Classes

class StoreUtil:
    @staticmethod
    def getAllProducts():
        all_products = []
        all_catalogProductEntity= CatalogProductEntity.objects.all()
        for entity in all_catalogProductEntity:
             all_products.append(Product(entity))
        return all_products

    @staticmethod
    def getAllCategoriesAtLevel(n, parent_id=False):
        all_categories = []
        all_catalogCategoryEntity= CatalogCategoryEntity.objects.all()
        for entity in all_catalogCategoryEntity:
             if entity.level == n:  
                 if (parent_id and entity.parent_id == parent_id) or not parent_id:    
                     all_categories.append(Category(entity))
        return all_categories



class Util:
     @staticmethod
     def parseToFloatRoundedTo2(number):
         return float("{0:.2f}".format(number))

class Category:
    def __init__(self, catalogCategoryEntity):
        self.id = catalogCategoryEntity.entity_id
        self.name = CatalogCategoryEntityVarchar.objects.get(entity_id=self.id, attribute_id= 41).value
        self.level = catalogCategoryEntity.level
        self.page_title = CatalogCategoryEntityVarchar.objects.get(entity_id=self.id, attribute_id= 46).value
        self.description = CatalogCategoryEntityText.objects.get(entity_id=self.id, attribute_id=44).value 
        self.products = []

    def setProducts(self):
        all_catalogCategoryProduct= CatalogCategoryProduct.objects.filter(category_id=self.id).values_list('product_id')
        self.info = all_catalogCategoryProduct
        for product_id in all_catalogCategoryProduct:
             entity = CatalogProductEntity.objects.get(entity_id = product_id[0])
             self.products.append(Product(entity))

class Product :
    def __init__(self, catalogProductEntity):
        self.id = catalogProductEntity.entity_id
        self.sku = catalogProductEntity.sku
        self.short_desc = CatalogProductEntityText.objects.get(entity_id=self.id,attribute_id=73).value
        self.long_desc = CatalogProductEntityText.objects.get(entity_id=self.id,attribute_id=72).value
        self.name = CatalogProductEntityVarchar.objects.get(entity_id=self.id,attribute_id=71).value       
        self.price = Util.parseToFloatRoundedTo2(CatalogProductEntityDecimal.objects.get(entity_id=self.id,attribute_id=75).value)
        self.weight = Util.parseToFloatRoundedTo2(CatalogProductEntityDecimal.objects.get(entity_id=self.id,attribute_id=80).value)
        self.quantity = int(CataloginventoryStockItem.objects.get(product_id=self.id).qty)

# Controllers

def homepage_view(request):
    response = {}
    response['all_categories']=StoreUtil.getAllCategoriesAtLevel(2)
    response['all_products']=StoreUtil.getAllProducts()
    return render(request, 'homePage.html', response)
     
def categorypage_view(request,category_id):
    response={}
    current_catalogCategoryEntity = CatalogCategoryEntity.objects.get(entity_id = category_id)
    current_category = Category(current_catalogCategoryEntity)
    current_category.setProducts()
    response['all_subcategories']= StoreUtil.getAllCategoriesAtLevel(current_category.level, current_category.id)
    response['all_products']= current_category.products
    response['category']= current_category
    return render(request, 'categoryPage.html', response)

def itempage_view(request,item_id):
    response = {}
    current_catalogProductEntity = CatalogProductEntity.objects.get(entity_id = item_id)
    current_product = Product(current_catalogProductEntity)
    response['all_categories']=StoreUtil.getAllCategoriesAtLevel(2)
    response['product']=current_product
    return render(request, 'itemPage.html', response)


