"""
Django settings for django3 project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from django.urls.base import reverse_lazy
from django.conf.global_settings import AUTHENTICATION_BACKENDS
'''
reverse_lazy와 reverse 공통점
등록된 URL의 별칭을 바탕으로 URL을 찾는 함수
차이점 - URL을 반환하는 시기
reverse : 함수 호출이 되자마자 등록된 URL에서 찾음
reverse_lazy : 웹서버가 정상적으로 실행된 뒤에 등록된
               URL을 찾음
setting.py는 웹서버가 실행되기위한 설정값이 있는파일이므로
URL Conf가 설정되지 않은 상태. 따라서 reverse를 사용할 수 없음
'''
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#로그인페이지가 있는 URL 주소
LOGIN_URL = reverse_lazy('cl:signin')
#로그인에 성공한 뒤 이동할 URL 주소 저장 변수
#소셜로그인을 사용한 클라이언트가 이동할 주소를 저장하는 용도
LOGIN_REDIRECE_URL = reverse_lazy('vote:index')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+p9yx&rgp6y9gwv40yipb4prxba)z2b^b)d^--)n*n1f$047(v'

# SECURITY WARNING: don't run with debug turned on in production!
#개발이 끝나면 DEBUG 변수에 False 값을 저장해
#에러코드를 숨김
DEBUG = False
#허용된 도메인주소(127.0.0.1:8000)만 웹서버에 접속할수있도록
#설정하는 변수
#웹클라이언트는 127.0.0.1이나 XXX(회원이름).pythonanywhere.com
#으로 시작하는웹주소만 웹서버에 접속할 수 있음
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookmark',
    'vote',
    'customlogin',
    #소셜로그인 관련 어플리케이션
    'social_django',
    'blog',
]
#인증 관련 모듈을 추가
AUTHENTICATION_BACKENDS = (
    #구글로그인 처리 관련 파이썬 클래스 추가
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GooglePlusAuth',
    #소셜로그인 정보를 Django의 User모델클래스에 저장처리하는 클래스
    'django.contrib.auth.backends.ModelBackend'
    )
#구글 개발사 사이트에서 발급한 ID, PASSWORD 저장변수
SOCIAL_AUTH_GOOGLE_PLUS_KEY = '155212801157-a4dt27a15376etpgi1vqlrgpkvjr8apd.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_PLUS_SECRET = '0jxXVOyvl0namiF9NQc0V0UG'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django3.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #소셜로그인 처리를 위한 템플릿관련함수 추가
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'django3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

#사용자가 업로드한 미디어파일(이미지,첨부파일)
#을 다운받을 수 있도록 설정
#MEDIA_URL : 클라이언트가 URL주소로 파일을 요청할때 사용하는
#            URL 저장 변수
#MEDIA_ROOT : 실제 파일이 저장되는 하드웨어 경로

#웹 클라이언트의 URL이 127.0.0.1:8000/files/로 시작하면
#파일을 요청하는 것으로 판단함
MEDIA_URL = '/files/'

#BASE_DIR : 현재 웹서버 프로젝트가 위치한 하드웨어 경로
#os.path.join : 파일경로를 생성하는 함수
MEDIA_ROOT = os.path.join(BASE_DIR,'files')

#클라이언트가 127.0.0.1:8000/files/test/1.jpg 로 요청하면
#웹서버 프로젝트가 있는 폴더의 files/test/1.jpg 파일을
#클라이언트에게 전송함