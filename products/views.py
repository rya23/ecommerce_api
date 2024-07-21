from django.http import JsonResponse
from products.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import generics

# Create your views here.


# @api_view(["GET", "POST"])
# def home(request):
#     body = request.body
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         data = ProductSerializer(instance).data

#     # serializer = ProductSerializer(data=request.data)
#     # if serializer.is_valid(raise_exception=True):

#     #     instance = serializer.save()
#     #     print(instance)
#     #     return Response(serializer.data)
#     return Response(data)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content=content)
        print(serializer.validated_data)


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
