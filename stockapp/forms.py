from django import forms 
from django.contrib.auth import get_user_model
from stockapp.models import Attendance, Employee,Overtime,Bonus
User = get_user_model()

class EmployeeCreationForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name','last_name', 'contact_no','email','password','salary','tax_rate','join_date','work_status']
        #For Label tag
        labels = {  
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'contact_no': 'Contact No',
            'email':'Email',
            'password': 'Password',
            'salary':'Salary',
            'tax_rate':'Tax Rate',
            'join_date':'Join Date',
            'work_status':'Work status'
        }
        
class AttendenceCreationForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['status','date', 'employee','no_of_absent_days']
        #For Label tag
        labels = {  
            'status': 'Status',
            'date': 'Date',
            'employee': 'Employee',
            'no_of_absent_days':'No of absent days',
     
        }


class OvertimeCreationForm(forms.ModelForm):
    class Meta:
        model = Overtime
        fields = ['employee','date','workInHour']
        #For Label tag
        labels = {  
            'employee': 'Employee',
            'date': 'Date',
            'workInHour': 'Work in hour',     
        }

class BonusCreationForm(forms.ModelForm):
    class Meta:
        model = Bonus
        fields = ['employee','date','occation','bonus_price']
        #For Label tag
        labels = {  
            'employee': 'Employee',
            'date': 'Date',
            'occation': 'Occation',     
            'bonus_price':'Bonus price'
        }
