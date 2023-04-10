# админ панель
from django.contrib import admin
# path и include для работы с путями
from django.urls import path, include
# настройки приложений
from django.conf import settings
# static для работы с путями статических файлов(изображения, архивы, иконки и т.д)
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
