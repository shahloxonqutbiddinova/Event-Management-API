from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.category import (
    CategoryListAPIView, CategoryCreateAPIView,
    CategoryDetailAPIView, CategoryUpdateAPIView, CategoryDeleteAPIView
)
from api.views.event import EventViewSet


router = DefaultRouter()
router.register(r"events", EventViewSet, basename="event")

urlpatterns = [
    path("accounts/", include("api.accounts.urls")),

    path("categories/", CategoryListAPIView.as_view(), name="category-list"),
    path("categories/create/", CategoryCreateAPIView.as_view(), name="category-create"),
    path("categories/<int:pk>/", CategoryDetailAPIView.as_view(), name="category-detail"),
    path("categories/<int:pk>/update/", CategoryUpdateAPIView.as_view(), name="category-update"),
    path("categories/<int:pk>/delete/", CategoryDeleteAPIView.as_view(), name="category-delete"),
]

urlpatterns += router.urls