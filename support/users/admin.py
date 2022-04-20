from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'is_support',
    )
    search_fields = ('username', 'email')
    list_filter = ('is_support',)
    readonly_fields = ('id',)
