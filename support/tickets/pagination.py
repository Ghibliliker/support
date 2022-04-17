from rest_framework.pagination import PageNumberPagination


class TicketCommentPagination(PageNumberPagination):
    page_size = 5
