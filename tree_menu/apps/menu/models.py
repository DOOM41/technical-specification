from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    CASCADE,
    Manager
)
from django.db.models import QuerySet


class MenuManager(Manager):
    def get_menu_and_submenu_items(self, name: str = '') -> dict:
        if not name:
            menu: QuerySet[Menu] = Menu.objects.all()
            sub_menu: QuerySet[SubMenu] = SubMenu.objects.all()
        else:
            menu: QuerySet[Menu] = Menu.objects.filter(name=name)
            sub_menu: QuerySet[SubMenu] = SubMenu.objects.filter(menu=menu.first())
        result = {}
        for menu_item in menu:
            result[menu_item] = sub_menu.filter(menu=menu_item)
        return result


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
