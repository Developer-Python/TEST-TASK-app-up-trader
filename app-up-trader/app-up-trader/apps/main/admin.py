
# Модуль для работы с Админ панелью
from django.contrib import admin

# Получение всех моделей
from . models import Category, Menu, Page

admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(Page)