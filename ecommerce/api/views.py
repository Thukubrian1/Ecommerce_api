from rest_framework import generics
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

# Category Views
class CategoryListCreateView(generics.ListCreateAPIView):
    """
    Handles listing all categories and creating a new category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a category by ID.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Product Views
class ProductListCreateView(generics.ListCreateAPIView):
    """
    Handles listing all products and creating a new product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a product by ID.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
