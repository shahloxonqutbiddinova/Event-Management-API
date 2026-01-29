from django.urls import path, include
from api.views.category import (
    CategoryListAPIView, CategoryCreateAPIView,
    CategoryDetailAPIView, CategoryUpdateAPIView, CategoryDeleteAPIView
)

urlpatterns = [
    path("accounts/", include("api.accounts.urls")),

    path("categories/", CategoryListAPIView.as_view(), name="category-list"),
    path("categories/create/", CategoryCreateAPIView.as_view(), name="category-create"),
    path("categories/<int:pk>/", CategoryDetailAPIView.as_view(), name="category-detail"),
    path("categories/<int:pk>/update/", CategoryUpdateAPIView.as_view(), name="category-update"),
    path("categories/<int:pk>/delete/", CategoryDeleteAPIView.as_view(), name="category-delete"),

]