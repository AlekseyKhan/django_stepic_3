from django.http import Http404
from django.shortcuts import render
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
            raise Http404(f'Страница не найдена!')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if 'category' not in self.kwargs:
            context['specialty_name'] = 'Все вакансии'
        else:
            try:
                context['specialty_name'] = Specialty.objects.get(code=self.kwargs['category']).title
            except Specialty.MultipleObjectsReturned:
                raise Http404(f'Возникла ошибка при обращении на страницу \"{self.kwargs["category"]}\" !')

        return context


class VacancyView(DetailView):
    template_name = 'vacancies/vacancy.html'
    model = Vacancy
    context_object_name = 'vacancy'
    pk_url_kwarg = 'vacancy_id'

    # def get_context_data(self, **kwargs):
    #     context = super(VacancyView, self).get_context_data(**kwargs)
    #     return context


class CompanyView(DetailView):
    template_name = 'vacancies/company.html'
    model = Company
    context_object_name = 'company'
    pk_url_kwarg = 'company_id'

    # def get_context_data(self, **kwargs):
    #     context = super(CompanyView, self).get_context_data(**kwargs)
    #     return context

# def vacancy_view(request, vacancy_id):
#     return render(request, 'vacancies/vacancy.html', context={
#         id: vacancy_id
#     })
