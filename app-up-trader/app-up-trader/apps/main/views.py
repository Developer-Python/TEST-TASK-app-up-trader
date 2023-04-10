
# Библеотека для работы с запросами и редиректами
from django.shortcuts import render

# Библеотека для работы с представлениями на основе классов предназначеный для отображения данных
from django.views.generic.base import View

# Модели приложенния
from . models import Menu, Page



class ListView(View):

    '''======================================================'''
    '''      Класс: Для отображение "Начальной страницы"     '''
    '''======================================================'''

    def get(self, request):
        
        menu = Menu.objects.all()
        category = menu
        
        return render(request, 'main/list.html', {'category': category, 'all_menu': menu})



class DetailView(View):

    '''==============================================='''
    '''     Класс: Для вывода "Детальной страницы"    '''
    '''==============================================='''

    def get(self, request, main_id):
        
        page = Page.objects.get(link_page=main_id)
        menu = page.included_menu.all()
        category = menu
        
        return render(request, 'main/detail.html', {'category': category, 'menu': menu, 'page': page})
