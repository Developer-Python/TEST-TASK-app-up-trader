# Модули для работы с [Системой]
import os, sys

# Каталог \app-up-trader\
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Изменнёная директория для поиска приложений в \apps\
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

# Использовать режим отладки
DEBUG = True

# Защита подписанных данных
SECRET_KEY = '12345test'

# Разрешённые хосты
ALLOWED_HOSTS = ['*']

# Список установленных приложений
INSTALLED_APPS = [

    # Стандартные приложения
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Мои приложения
    'main.apps.MainConfig',

]

# Промежуточный слой
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Главная конфигурация ссылок
ROOT_URLCONF = 'app-up-trader.urls'

# Шаблоны
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # Использование шаблонов из папки \templates\
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates')],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Выступает в роли простого сервера [WSGI]
WSGI_APPLICATION = 'app-up-trader.wsgi.application'

# База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Управления пользовательскими паролями.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Язык
LANGUAGE_CODE = 'ru'

# Часовой пояс
TIME_ZONE = 'UTC'

# Использовать механизм перевода Django ?
USE_I18N = True

# Использовать локализованный формат даты ?
USE_L10N = False

# Использовать часовой пояс ?
USE_TZ = True

# Настройка статических файлов
STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# Настройка динамичных файлов
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

