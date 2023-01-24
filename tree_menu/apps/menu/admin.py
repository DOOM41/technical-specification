from django.contrib import admin
from menu.models import Menu, SubMenu

# Register your models here.


class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    list_filter = (
        'name',
    )


class SubMenuAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'menu',
    )
    list_filter = (
        'menu',
    )


admin.site.register(Menu, MenuAdmin)
admin.site.register(SubMenu, SubMenuAdmin)
