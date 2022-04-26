from django.urls import path

from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='homepage'),
    path('vacancies/', VacanciesView.as_view(), name='vacancies_page'),
    path('vacancies/cat/<str:category>/', VacanciesView.as_view(), name='vac_by_spec_page'),
    path('company/', CompanyView.as_view(), name='company_page'),
    path('vacancy/<int:vacancy_id>/', VacancyView.as_view(), name='vacancy_page'),
]