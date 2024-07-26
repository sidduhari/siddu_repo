from django import forms
from testapp.models import Employee
from django.core import validators
class EmployeeForm(forms.ModelForm):
    name = forms.CharField()
    phone_number = forms.IntegerField()
    class Meta:
        model = Employee
        fields = '__all__'
    #
    # def clean(self):
    #     print('validating name field')
    #     total_clean_data=super().clean()
    #     print('validating name')
    #     inputname = self.cleaned_data['name']
    #     if inputname[0].lower:
    #         raise forms.ValidationError('starting number Capital')