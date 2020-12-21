from rest_framework import serializers
from .models import Product,Category,Store,Item,Order,IncomeProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:  
        model = Product
        #store_name = serializers.ReadOnlyField(source = 'store_name.store')
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    store_name = serializers.SlugRelatedField(read_only=False,slug_field='store',queryset = Store.objects.all())
    item = serializers.SlugRelatedField(read_only=False,slug_field='product_name',queryset = Product.objects.all())
    class Meta:  
        model = Item
        fields = ['id','url','store_name','item','quantity']
        #depth = 1
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id','url','store','description']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','url','category_name']

class IncomeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeProduct
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'