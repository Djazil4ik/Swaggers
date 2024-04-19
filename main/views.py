from rest_framework import generics
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product

class ProductApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer