from django.http import Http404, HttpResponseNotFound
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

# Create your views here.
from vacancies.models import Specialty, Company, Vacancy


class MainView(TemplateView):
    template_name = 'vacancies/index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['specialities'] = Specialty.objects.all()
        context['companies'] = Company.objects.all()
        context['head_title'] = 'Джуманджи - Главная страница'
        return context


class VacanciesView(ListView):
    template_name = 'vacancies/vacancies.html'
    model = Vacancy
    context_object_name = 'vacancies_list'

    def get_queryset(self):
        if 'category' not in self.kwargs:
            return Vacancy.objects.all()
        elif self.kwargs['category'] in {s.code for s in Specialty.objects.all()}:
            return Vacancy.objects.filter(specialty__code=self.kwargs['category'])
        else:
            raise Http404('Страница не найдена!')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if 'category' not in self.kwargs:
            context['specialty_name'] = 'Все вакансии'
            context['head_title'] = 'Джуманджи - Все вакансии'
        else:
            context['specialty_name'] = Specialty.objects.filter(code=self.kwargs['category'])[0].title
            context['head_title'] = f"Джуманджи - {context['specialty_name']}"

        return context


class VacancyView(DetailView):
    template_name = 'vacancies/vacancy.html'
    model = Vacancy
    context_object_name = 'vacancy'
    pk_url_kwarg = 'vacancy_id'

    def get_context_data(self, **kwargs):
        context = super(VacancyView, self).get_context_data(**kwargs)
        context['head_title'] = f"Джуманджи - {Vacancy.objects.filter(pk=self.kwargs['vacancy_id'])[0].title}"
        return context


class CompanyView(DetailView):
    template_name = 'vacancies/company.html'
    model = Company
    context_object_name = 'company'
    pk_url_kwarg = 'company_id'

    def get_context_data(self, **kwargs):
        context = super(CompanyView, self).get_context_data(**kwargs)
        context['head_title'] = f"Джуманджи - {Company.objects.filter(pk=self.kwargs['company_id'])[0].name}"

        return context
