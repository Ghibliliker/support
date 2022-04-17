from django.urls import include, path
from rest_framework.routers import DefaultRouter

from tickets.views import TicketViewSet, CommentViewSet

router = DefaultRouter()

router.register(r'tickets', TicketViewSet)
router.register(r'tickets/(?P<ticket_id>\d+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
]
