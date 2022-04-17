from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response

from support.tasks import send_mail_user
from tickets.pagination import TicketCommentPagination
from tickets.models import Ticket
from tickets.permissions import (OwnerOrReadOnly,
                                 OwnerOrSupportOrReadOnly,
                                 SupportOnly)
from tickets.serializers import (TicketListSerializer,
                                 CommentListSerializer,
                                 CommentCreateSerializer,
                                 TicketCreateSerializer,
                                 TicketStatusSerializer)


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    permission_classes = [OwnerOrReadOnly]
    pagination_class = TicketCommentPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter)
    filterset_fields = ('status',)
    search_fields = ('^name',)
    ordering_fields = ('name', 'pub_date')
    ordering = ('pub_date',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TicketListSerializer
        return TicketCreateSerializer

    @action(
        detail=True,
        permission_classes=(SupportOnly,),
        methods=['PATCH'])
    def status(self, request, pk):
        obj = self.get_object()
        user_email = obj.author.email
        serializer = TicketStatusSerializer(
            obj,
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        send_mail_user.delay(user_email)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentViewSet(viewsets.ModelViewSet):
    pagination_class = TicketCommentPagination
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('pub_date',)
    ordering = ('pub_date',)

    def get_queryset(self):
        ticket = get_object_or_404(Ticket, pk=self.kwargs.get('ticket_id'))
        return ticket.comments.all()

    def get_permissions(self):
        ticket = get_object_or_404(Ticket, pk=self.kwargs.get('ticket_id'))
        if ticket.author == self.request.user:
            permission_classes = [OwnerOrReadOnly]
        else:
            permission_classes = [OwnerOrSupportOrReadOnly]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        ticket = get_object_or_404(Ticket, pk=self.kwargs.get('ticket_id'))
        serializer.save(author=self.request.user, ticket=ticket)

    def perform_update(self, serializer):
        ticket = get_object_or_404(Ticket, pk=self.kwargs.get('ticket_id'))
        serializer.save(author=self.request.user, ticket=ticket)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return CommentListSerializer
        return CommentCreateSerializer
