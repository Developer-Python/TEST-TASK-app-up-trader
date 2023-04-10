
# Модуль для работы с моделями
from django.db import models



class Category(models.Model):

	'''============================='''
	'''       Модель: Категория     '''
	'''============================='''

	id = models.AutoField(primary_key=True)
	name = models.CharField(verbose_name='Название категорий', max_length=50)
	discription = models.CharField(verbose_name='Подкатегория', max_length=50)

	def __str__(self):
		return f' {self.name}'

	class Meta:
		verbose_name = 'Новая категория'
		verbose_name_plural = 'Категории'



class Menu(models.Model):

	'''============================='''
	'''         Модель: Меню        '''
	'''============================='''

	name_menu = models.CharField(verbose_name='Название меню', max_length=50)
	included_categories = models.ManyToManyField(Category, verbose_name='Список категорий в данном меню', blank=True, related_name='included_categories')
	

	def __str__(self):
		return f' {self.name_menu}'
	
	class Meta:
		verbose_name = 'Новое меню'
		verbose_name_plural = 'Меню'



class Page(models.Model):

	'''================================='''
	'''         Модель: Страница        '''
	'''================================='''

	link_page = models.IntegerField(verbose_name="Ввидите номер страницы к которой добавить меню", blank=True)
	included_menu = models.ManyToManyField(Menu, verbose_name='Какие меню добавить на страницу', blank=True, related_name='included_menu')

	def __str__(self):
		return f' {self.link_page}'

	class Meta:
		verbose_name = 'Страница'
		verbose_name_plural = 'Страницы'