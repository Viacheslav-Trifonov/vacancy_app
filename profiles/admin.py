from django.contrib import admin

from vacancy.models import Company, Specialty, Vacancy


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'employee_count']
    list_editable = ['location', 'employee_count']
    ordering = ['name']
    list_per_page = 20
    search_fields = ['name', 'location', 'employee_count']
    list_filter = ['name', 'location', 'employee_count']

@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ['code', 'title']
    list_editable = ['title']
    ordering = ['code']
    list_per_page = 20
    search_fields = ['code', 'title']
    list_filter = ['code', 'title']


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'specialty', 'company', 'salary_min', 'salary_max']
    list_editable = ['specialty', 'company', 'salary_min', 'salary_max']
    ordering = ['title']
    list_per_page = 20
    search_fields = ['title', 'specialty', 'company', 'salary_min', 'salary_max']
    list_filter = ['title', 'specialty', 'company', 'salary_min', 'salary_max']
