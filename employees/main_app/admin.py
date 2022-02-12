from django.contrib import admin

from employees.main_app.models import Company, Employee


# to show employee_set of the Company in db admin
class EmployeeInlineAdmin(admin.StackedInline):
    model = Employee


@admin.register(Company)
class baseCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'turnover')

    inlines = (EmployeeInlineAdmin,)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('f_name', 'l_name', 'date_of_birth', 'position', 'employer')
