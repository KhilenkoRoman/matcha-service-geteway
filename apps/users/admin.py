from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext, gettext_lazy as _
from apps.users.models import User, UserInfo


class UserInfoInline(admin.StackedInline):
    model = UserInfo


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email',)
    readonly_fields = ("date_joined",)
    inlines = (UserInfoInline,)

    # override fieldsets to remove groups permissions
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', )}),
        (_('Permissions'), {
            'fields': ('is_active', ),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
        (_('Permissions'), {
            'fields': ('is_active', ),
        }),
        (_('Personal info'), {'fields': ('first_name', 'last_name',)}),
    )
    ordering = ('email',)
    search_fields = ['email']


# unregister default Django and All Auth app model in admin
admin.site.unregister(Group)
