from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from api.models.event import Event
from api.serializers.event import EventSerializer
from api.permissions import EventPermission

class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [EventPermission]

    queryset = Event.objects.filter(is_active=True)

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "description", "location"]
    ordering_fields = ["start_time", "created_at", "title"]
    ordering = ["start_time"]

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category_id=category)
        status = self.request.query_params.get("status")
        if status:
            queryset = queryset.filter(status=status)

        return queryset