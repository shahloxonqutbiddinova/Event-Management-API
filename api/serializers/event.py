from rest_framework import serializers
from django.utils import timezone

from api.models.event import Event
from api.models.category import Category

class EventSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.filter(is_active = True))

    class Meta:
        model = Event
        fields = ["id", "title", "slug", "description", "category", "location",
                  "start_time", "end_time", "status", "owner", "created_at", "updated_at",]
        read_only_fields = ["id", "slug", "ower", "created_at", "updated_at",]

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return value

    def validate_description(self, value):
        if len(value) <20:
            raise serializers.ValidationError("Description must be at least 20 characters long.")
        return value

    def validate(self, attrs):
        start_time = attrs.get("start_time")
        end_time = attrs.get("end_time")

        if start_time and end_time:
            if start_time >= end_time:
                raise serializers.ValidationError("End time must be later than start time.")

            if start_time < timezone.now():
                raise serializers.ValidationError("Event start time cannot be in the past.")
        return attrs

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["owner"] = request.user
        return super().create(validated_data)
