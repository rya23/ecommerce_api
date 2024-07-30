from django.http import JsonResponse
from products.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import generics, permissions, authentication
from .permissions import *


# Create your views here.
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content=content)
        print(serializer.validated_data)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsStaffEditorPermissions]

    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        # serializer.save(user=self.request.user)
        instance = serializer.save()
        if not instance.content:
            serializer.content = serializer.title
        print(serializer.validated_data)


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        # serializer.save(user=self.request.user)
        super().perform_destroy(instance)


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


class CartListAPIView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartUpdateAPIView(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = "pk"


class CartDeleteAPIView(generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        # serializer.save(user=self.request.user)
        super().perform_destroy(instance)
