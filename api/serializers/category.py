from rest_framework import serializers
from api.models.category import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug", "is_active", "created_at"]
        read_only_fields = ["id", "slug", "created_at"]

