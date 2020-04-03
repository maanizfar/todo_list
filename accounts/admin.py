from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_joined',
                    'last_login', 'is_admin', 'is_staff',)
    readonly_fields = ('date_joined', 'last_login')
    search_fields = ('username', 'email')

    filter_horizontal = ()
    fieldsets = ()
    list_filter = ()


admin.site.register(CustomUser, CustomUserAdmin)
