from django.contrib import admin

from tickets.models import Comment, Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'status', 'author', 'pub_date')
    search_fields = ('name', 'author')
    list_filter = ('status', 'pub_date')
    readonly_fields = ('id',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket', 'text', 'author', 'pub_date')
    search_fields = ('ticket', 'author')
    list_filter = ('pub_date', 'ticket')
    readonly_fields = ('id',)
