from django.urls import path
from .views import Products, ProductUpdateView, ProductDeleteView, ProductCreateView, ProductDetailView

urlpatterns = [
    path('', Products.as_view()),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Ссылка на детали товара
    path('create/', ProductCreateView.as_view(), name='product_create'),  # Ссылка на создание товар
    path('create/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
]
