
from django.db import models
from django.contrib.auth.models import User
from .utils import choice,workchoice


class Contact(models.Model):
    name=models.CharField(max_length=250,null=True)
    number=models.CharField(max_length=250,null=True)
    subject=models.CharField(max_length=250,null=True)
    message=models.TextField(null=True)

    def __str__(self):
        return self.number
        
class Category(models.Model):
    cat_name=models.CharField(max_length=250,null=True)
    cat_img=models.FileField(upload_to="media",null=True)
    cat_desc=models.TextField(max_length=250,null=True)
    added_on=models.DateTimeField(null=True)

    def __str__(self):
        return self.cat_name


class Register(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    profile=models.ImageField(upload_to="media")
    contact_number=models.IntegerField(null=True)
    age=models.IntegerField(null=True)
    gender=models.CharField(max_length=250,null=True)
    occupation=models.TextField(max_length=250,null=True)
    added_on=models.DateTimeField(null=True)
    update_on=models.DateTimeField(null=True)

    def __str__(self):
        return self.user.username


class Employee(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    tax=models.FloatField(max_length=250,default=0)
    salary=models.FloatField(max_length=250,default=0,null=True)
    join=models.CharField(max_length=250,default=0,null=True)
    overtimehour = models.FloatField(max_length=250)
    bonus = models.FloatField(max_length=250,default=0)
    no_of_leave_day = models.FloatField(max_length=250,default=0)
    work_status = models.CharField(max_length=250,choices=workchoice)

    # def __str__(self):
    #     return self.user.first_name

    
    @property
    def total_salary(self):
        perdayleave = self.salary/25
        tax_rate = self.tax/100
        overtimecost = 100
        tax_deduction = tax_rate*self.salary
        overtimepay = self.overtimehour*overtimecost
        leave_cut = self.no_of_leave_day*perdayleave
        
        totalsalary = self.salary+float(self.bonus)+float(overtimepay)-tax_deduction-leave_cut  
        return totalsalary



class Attendance(models.Model):    
    status = models.CharField(choices=choice,max_length=250)
    date = models.DateField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    # created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)




        # perdayleave = (int(self.employee.salary))/2

        # taxrate = int(self.employee.tax)/100
        # salary= int(self.employee.salary)
        # bonus = int(self.bonus)
        # overtimecost=100
        # taxdeduction = (taxrate)*salary
        # overtimepay = int(self.employee.overtimehour)*overtimecost  
        # leave_cut = int(self.attendece.no_of_leave_day)*perdayleave
        # totalsalary = salary+bonus+overtimepay-taxdeduction-leave_cut  
        #   
