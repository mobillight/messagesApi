from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet

from messages.models import Message
from messages.serializers import MessageSerializer


class MessagesView(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def get_queryset(self):
        user_id = self.request.GET.get('user_id')
        if user_id:
            if self.action in ['list', 'retrieve', 'destroy']:
                return self.queryset.filter(Q(receiver=user_id) | Q(sender=user_id))
            if self.action == 'unread':
                return self.queryset.filter(receiver=user_id)
        return self.queryset.none()

    @action(methods=['get'], detail=False)
    def unread(self, request):
        return Response(data=self.serializer_class(self.get_queryset(), many=True).data)
