from django.urls import path

from .views import MainView, VacanciesView, CompanyView, VacancyView

urlpatterns = [
    path('', MainView.as_view(), name='homepage'),
    path('vacancies/', VacanciesView.as_view(), name='vacancies_page'),
    path('vacancies/cat/<str:category>/', VacanciesView.as_view(), name='vacancies_by_page'),
    path('company/<int:company_id>', CompanyView.as_view(), name='company_page'),
    path('vacancies/<int:vacancy_id>/', VacancyView.as_view(), name='vacancy_page'),
]
