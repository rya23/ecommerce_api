from django.urls import path
from . import views


urlpatterns = [
    path("<int:pk>/", views.ProductDetailAPIView.as_view()),
    path("", views.ProductListCreateAPIView.as_view()),
    path("<int:pk>/update/", views.ProductUpdateAPIView.as_view()),
    path("<int:pk>/delete/", views.ProductDeleteAPIView.as_view()),
    path("cart/", views.CartListCreateAPIView.as_view()),
    path("cart/<int:pk>/delete/", views.CartDeleteAPIView.as_view()),
    path("cart/<int:pk>/update/", views.CartUpdateAPIView.as_view()),
]
