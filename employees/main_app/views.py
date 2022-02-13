from django.shortcuts import render, HttpResponse, redirect

from employees.main_app.forms import CreateEmployeeForm, CreateEmployeeModelForm, UpdateEmployeeForm
from employees.main_app.models import Employee, Company


def home(request):
    # return HttpResponse('it works!')

    employees = Employee.objects.all()
    return render(request,
                  'main_app/home.html',
                  {'employees': employees})


def create_employee_with_basic_form(request):
    if request.method == "POST":
        new_employee_form = CreateEmployeeForm(request.POST)
        if new_employee_form.is_valid():
            # emp = Employee(**new_employee_form.cleaned_data)
            # Above doesn't work because form returns str not Company instance
            employer_name = new_employee_form.cleaned_data['employer']
            employer = Company.objects.get(name=employer_name)

            emp = Employee(
                f_name=new_employee_form.cleaned_data['f_name'],
                l_name=new_employee_form.cleaned_data['l_name'],
                position=new_employee_form.cleaned_data['position'],
                date_of_birth=new_employee_form.cleaned_data['date_of_birth'],
                employer=employer
            )

            emp.save()
            return redirect('home')
    # if request is POST but validation fails, we still have form with prefilled fields + errors from above
    else:
        new_employee_form = CreateEmployeeForm()
    context = {'new_employee_form': new_employee_form}

    return render(request, 'main_app/create_basic.html', context)


def create_employee_with_model_form(request):
    if request.method == "GET":
        form = CreateEmployeeModelForm()
        return render(request, 'main_app/create_model.html', {'form': form})

    else:
        form = CreateEmployeeModelForm(request.POST)
        if form.is_valid():
            employee = form.save()
            employee.save()
            return redirect('home')

        # What if post ot not is_valid()?
        return render(request, 'main_app/create_model.html', {'form': form})


def update_employee(request, pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == 'POST':
        employee_form = UpdateEmployeeForm(
            request.POST,
            instance=employee,
        )
        if employee_form.is_valid():
            employee_form.save()
            return redirect('home')
    else:
        employee_form = UpdateEmployeeForm()

    context = {
        'employee': employee,
        'employee_form': employee_form,
    }

    return render(request, 'main_app/update.html', context)


def delete_employee(request, pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('home')

    else:
        return render(request, 'main_app/delete.html', {'employee': employee})
