from django.urls import path,include
from rest_framework import routers
from .import views

# ItemList = views.ItemViewSet.as_view({
#         'get': 'list',
#         'post': 'create'
#     })
# ItemDetail = views.ItemViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
router = routers.DefaultRouter()
router.register('items',views.ItemViewSet)
router.register('stores',views.StoreViewSet)
router.register('categories',views.CategoryViewSet)
router.register('incomeproducts',views.IncomeProductViewSet)


urlpatterns = [
    #path('',views.cost_all,name = 'cost-all'),
    path('',include(router.urls)),
    path('products/',views.ProductList.as_view()),
    path('products/<int:pk>/',views.ProductDetail.as_view()),
    # path('items/',ItemList),
    # path('items/<int:pk>/',ItemDetail)
    path('orders/',views.OrderList.as_view()),
    path('orders/<int:pk>/',views.OrderDetail.as_view()),
]
