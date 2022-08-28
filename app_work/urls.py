"""app_work URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from profiles.views import UserLoginView, UserSignupView
from vacancy.views import *

admin.site.site_header = 'Админ меню сайта "Вакансии'
admin.site.index_title = 'Админ меню'

handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main'),
    path('vacancies/', vacancies_view, name='vacancies'),
    path('vacancies/cat/<str:specialty>/', specialty_view, name='specialty'),
    path('companies/<int:company_id>/', company_view, name='company'),
    path('vacancies/<int:vacancy_id>/', vacancy_view, name='vacancy'),
    path('vacancies/<int:vacancy_id>/send/', send_request_view, name='send_request'),
    path('mycompany/', my_company_view, name='my_company'),
    path('mycompany/vacancies/', my_company_vacancies_view, name='my_company_vacancies'),
    path('mycompany/vacancies/create/', create_vacancy_view, name='create_vacancy'),
    path('mycompany/vacancies/<int:vacancy_id>/', my_company_vacancy_view, name='my_company_vacancy'),
    path('mycompany/create/', create_company_view, name='create_company'),
    path('mycompany/letsstart/', company_start_view, name='company_lets_start'),
    path('profile/', profile_view, name='profile'),
    path('search/', SearchView.as_view(), name='search'),
    path('myresume/letsstart/', resume_start_view, name='resume_lets_start'),
    path('myresume/create/', create_resume_view, name='create_resume'),
    path('myresume/', my_resume_view, name='my_resume'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', UserSignupView.as_view(), name='signup'),
            ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
