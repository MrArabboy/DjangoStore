from django.shortcuts import render
from .models import Order,Item,Product,Store,Category,IncomeProduct
from rest_framework import viewsets,status,permissions,mixins,generics,authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer,ItemSerializer,StoreSerializer,CategorySerializer,OrderSerializer,IncomeProductSerializer
from .permissions import IsOwnerOrReadOnly

def cost_all(request):        
    item = Order.objects.last()
    total = Order.objects.last().get_total_price
    context = {
        'item':item,
        'total':total,
    }
    return render(request,'products/total.html',context)

class ProductList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self,request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset,many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    #authentication_classes = [authentication.BaseAuthentication]
    permission_classes = [permissions.IsAdminUser]
    def get_object(self,pk):
        try :
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status = status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,pk):
        queryset = self.get_object(pk)
        serializer = ProductSerializer(queryset)
        return Response(serializer.data)

    def put(self,request,pk):
        queryset = self.get_object(pk)
        serializer = ProductSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ItemViewSet(viewsets.ModelViewSet):
    # #This viewset automatically provides `list`, `create`, `retrieve`,`update` and `destroy` actions.
    # Additionally we also provide an extra `highlight` action.
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]   #IsOwnerOrReadOnly

class IncomeProductViewSet(viewsets.ModelViewSet):
    queryset = IncomeProduct.objects.all()
    serializer_class = IncomeProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OrderList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class OrderDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

