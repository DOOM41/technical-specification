from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    CASCADE,
    Manager
)
from django.db.models import QuerySet


class MenuManager(Manager):
    def get_menu_and_submenu_items(self, name: str) -> dict:
        # Check name for some data
        if not name:
            sub_menu: QuerySet[SubMenu] = SubMenu.objects.all()
        else:
            sub_menu: QuerySet[SubMenu] = SubMenu.objects.filter(
                menu__name=name
            )
        # Make result dict 
        result = {}
        for menu_item in sub_menu:
            result[menu_item.menu.name] = sub_menu.filter(
                menu__name=menu_item.menu.name
            )
        # Sort data 
        sorted_dict = dict(sorted(result.items()))
        return sorted_dict


class Menu(Model):
    name = CharField(
        'Название элемента меню',
        null=False,
        max_length=100
    )
    objects = MenuManager()

    class Meta:
        ordering = (
            'name',
        )
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self) -> str:
        return self.name


class SubMenu(Model):
    name = CharField(
        'Название элемента сабкатегории',
        null=False,
        max_length=100
    )
    menu = ForeignKey(Menu, on_delete=CASCADE)

    class Meta:
        ordering = (
            'name',
        )
        verbose_name = 'Под меню'
        verbose_name_plural = 'Под меню'

    def __str__(self) -> str:
        return self.name
