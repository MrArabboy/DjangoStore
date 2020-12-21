from django.contrib import admin
from .models import Product,Order,Item,Category,Store,IncomeProduct

class ProductDisplay(admin.ModelAdmin):
    list_display = ['product_name','store_name','price_of_item','total_in_shop_now','total_after_income','product_added_time']


class OrderDisplay(admin.ModelAdmin):
    list_display = ['__str__','get_total_price','ordered_time','total_income_of_order']

class ItemDisplay(admin.ModelAdmin):
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "item":
    #         kwargs["queryset"] = Product.objects.filter(store_name__store__contains = str(Item.store_name) )
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ['__str__','get_total_item_price','get_total_item_income','market']

class IncomeProductDisplay(admin.ModelAdmin):
    list_display = ['product','store_name','quantity_of_income','date_income']

admin.site.register(Product,ProductDisplay) 
admin.site.register(Order,OrderDisplay)
admin.site.register(Item,ItemDisplay)
admin.site.register(Category)
admin.site.register(Store)
admin.site.register(IncomeProduct,IncomeProductDisplay)
