from django.urls import path

from .views import home, create_employee_with_basic_form, create_employee_with_model_form

urlpatterns = [
    path('', home, name="home"),
    path('create1/', create_employee_with_basic_form, name="create new employee 1"),
    path('create2/', create_employee_with_model_form, name="create new employee 2"),
]
