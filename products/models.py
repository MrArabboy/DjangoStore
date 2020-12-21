from django.db import models
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey

class Store(models.Model):
    store = models.CharField(max_length = 50)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.store

class Category(models.Model):
    category_name = models.CharField(max_length = 50)
    class Meta :
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.category_name

class Product(models.Model): 
    store_name = models.ForeignKey(Store,default = None,null=True,on_delete = models.DO_NOTHING)
    product_name = models.CharField(max_length = 25)
    select_category = models.ForeignKey(Category,on_delete = models.DO_NOTHING)
    description = models.TextField(null=True,blank=True)
    base_price = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    price_in_shop = models.DecimalField(max_digits=5,decimal_places=2,default=None)
    total_in_shop = models.DecimalField(max_digits=5,decimal_places=2,default=1)
    product_added_time = models.DateTimeField(default = timezone.now)

    def total_after_income(self):
        total = self.total_in_shop
        for product in IncomeProduct.objects.all():
            if str(product) == self.product_name and str(product.store_name) == self.store_name.store:
                total += product.quantity_of_income
        return total

    def total_in_shop_now(self):
        total = self.total_after_income()
        for item in Item.objects.all():
            if str(item.item) == self.product_name and str(item.store_name) == self.store_name.store :
                total -= item.quantity
        return f'{total}/{self.total_after_income()}'
    
    def price_of_item(self):
        return f"${self.price_in_shop}"
        
    def __str__(self):
        return self.product_name

class IncomeProduct(models.Model):
    store_name = models.ForeignKey(Store,default = None,null=True,on_delete = models.DO_NOTHING)
    product = models.ForeignKey(Product,on_delete = models.DO_NOTHING)
    quantity_of_income = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    date_income = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.product.product_name

class Item(models.Model):
    store_name = models.ForeignKey(Store,on_delete = models.DO_NOTHING,default= None,null=True)
    item = ChainedForeignKey(
        Product, 
        chained_field = 'store_name', #this is Item.store_name
        chained_model_field = 'store_name', #This is Product.store_name
        show_all = False,
        auto_choose = True,  #auto select the choice when there is only one available choice
        sort = True
        )
    quantity = models.PositiveIntegerField(default=1)
    
    def get_total_item_price(self):
        total = self.quantity * self.item.price_in_shop
        return f'${total}'

    def market(self):
        return self.store_name
    def get_total_item_income(self):
        total_item_income = self.quantity * self.item.price_in_shop - self.quantity * self.item.base_price
        return f'${total_item_income}'

    def __str__(self):
        return f"{self.quantity} of {self.item.product_name}"

class Order(models.Model):
    items = models.ManyToManyField(Item,blank=True)
    ordered_time = models.DateTimeField(default = timezone.now)

    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += float(order_item.get_total_item_price().lstrip('$'))
        return f"${round(total,2)}"

    def total_income_of_order(self):
        total_income = 0
        for order_item in self.items.all():
            total_income += float(order_item.get_total_item_income().lstrip('$'))
        return f"${round(total_income,3)}"
     
    def __str__(self):
        items=''
        for item in self.items.all():
            items += str(item)+' , '
        return items.rstrip(' , ')


