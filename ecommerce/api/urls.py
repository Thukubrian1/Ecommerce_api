from django.urls import path
from .views import (
    CategoryListCreateView,
    CategoryDetailView,
    ProductListCreateView,
    ProductDetailView
)
from .auth_views import ObtainAuthTokenView, LogoutView

urlpatterns = [
    # Category Endpoints
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    # Product Endpoints
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('auth/login/', ObtainAuthTokenView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
]