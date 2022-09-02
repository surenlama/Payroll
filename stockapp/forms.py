from django import forms 
from django import forms
from django.contrib.auth import get_user_model
from stockapp.models import Employee
User = get_user_model()

class EmployeeCreationForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name','last_name', 'contact_no','email','password','salary','tax_rate','join_date','no_of_absent_days','work_status']
        #For Label tag
        labels = {  
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'contact_no': 'Contact No',
            'email':'Email',
            'password': 'Password',
            'salary':'Salary',
            'tax_rate':'Tax Rate',
            'no_of_absent_days':'No of absent days',
            'join_date':'Join Date',
            'work_status':'Work status'
        }
        
    def save(self, commit=True):
        user = super().save()
        user_object = User.objects.create_user(username=self.cleaned_data["first_name"],email=self.cleaned_data["email"],password=self.cleaned_data["password"])
        user_object.first_name = self.cleaned_data["first_name"]
        user_object.last_name = self.cleaned_data["last_name"]

        user_object.is_active=True
        user_object.save()
        return user_object            

