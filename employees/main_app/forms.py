from django import forms
from .models import Company, Employee

POSITIONS = [
    ("A_position", "A_position"),
    ("B_position", "B_position"),
    ("C_position", "C_position"),
    ("D_position", "D_position"),
]

existing_companies = Company.objects.all()
employer_options = []
for company in existing_companies:
    choice_pair = (company, f'{company.name}')  # will write Company instance in DB, display just name
    # choice_pair = (company, company)
    employer_options.append(choice_pair)


class CreateEmployeeForm(forms.Form):
    f_name = forms.CharField(max_length=40, widget=forms.TextInput)
    l_name = forms.CharField(max_length=40)
    position = forms.ChoiceField(choices=POSITIONS)
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget)

    employer = forms.ChoiceField(choices=employer_options)


class CreateEmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class UpdateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
