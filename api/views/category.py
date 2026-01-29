from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models.category import Category
from api.serializers.category import CategorySerializer
from api.permissions import CategoryPermission


class CategoryListAPIView(APIView):
    permission_classes = [CategoryPermission]

    def get(self, request):
        categories = Category.objects.filter(is_active = True)
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class CategoryCreateAPIView(APIView):
    permission_classes = [CategoryPermission]

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CategoryDetailAPIView(APIView):
    permission_classes = [CategoryPermission]

    def get(self, request, pk):
        category = Category.objects.get(pk  =pk, is_active = True)
        serializer = CategorySerializer(category)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryUpdateAPIView(APIView):
    permission_classes = [CategoryPermission]

    def put(self, request, pk):
        category = Category.objects.get(pk=pk, is_active=True)
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryDeleteAPIView(APIView):
    permission_classes = [CategoryPermission]

    def delete(self, request, pk):
        category = Category.objects.get(pk=pk, is_active=True)
        category.is_active = False
        category.save(update_fields=["is_active"])

        return Response(status=status.HTTP_204_NO_CONTENT)
