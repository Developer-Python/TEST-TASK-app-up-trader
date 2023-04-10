
# Модуль для работы с путями
from django.urls import path

# Классы приложенния
from . import views

app_name = 'main'

urlpatterns = [
	path("", views.ListView.as_view(), name='category'),
    path('<int:main_id>/', views.DetailView.as_view(), name = 'detail'),
]
