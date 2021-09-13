from django import forms
from crud_app.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model =Employee
        fields ="__all__"

