from django import forms 
from django import forms
from django.contrib.auth import get_user_model
from stockapp.models import Employee
User = get_user_model()

class EmployeeCreationForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user','tax', 'salary','join','overtimehour','bonus','no_of_leave_day','work_status']
        #For Label tag
        labels = {  
            'user': 'User',
            'tax': 'Tax',
            'salary': 'Salary',
            'join':'Join',
            'overtimehour':'Over time in hour',
            'bonus':'Bonus',
            'no_of_leave_day':'No of leave days',
            'work_status':'Work status'
        }


