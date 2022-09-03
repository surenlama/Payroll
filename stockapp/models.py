from django.db import models
from django.contrib.auth.models import User
from .utils import choice,workchoice
import datetime


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


# class Employee(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    # tax=models.FloatField(max_length=250,default=0)
    # salary=models.FloatField(max_length=250,default=0,null=True)
    # join=models.CharField(max_length=250,default=0,null=True)
    # overtimehour = models.FloatField(max_length=250)
    # bonus = models.FloatField(max_length=250,default=0)
    # no_of_leave_day = models.FloatField(max_length=250,default=0)
class Employee(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=250,null=True)
    last_name = models.CharField(max_length=250,null=True)
    contact_no = models.CharField(max_length=250,null=True,blank=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=250,null=True)
    salary = models.FloatField(default=0)
    tax_rate = models.FloatField(default=0)
    join_date = models.DateField(null=True)    
    work_status = models.CharField(max_length=250,choices=workchoice)
    bankamount = models.FloatField(default=0)
    
    def __str__(self):
        return self.first_name

    @property
    def total_salary(self):
        absent = 0
        over = 0
        bonu=0
        attendence = self.attende.all()
        overtimes = self.overtime.all()
        bonuss = self.bonus.all()

        for i in attendence:
            absent=i.no_of_absent_days
        for j in overtimes:
            over=j.workInHour
        for k in bonuss:
            bonu=k.bonus_price            
        self.bankamount+=self.salary-(absent*(self.salary/24)-self.tax_rate/100*self.salary)+over*100+bonu
        self.save()
        return self.bankamount


class Attendance(models.Model):    
    status = models.CharField(choices=choice,max_length=250)
    date = models.DateField(null=True)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True,blank=True,related_name="attende")
    no_of_absent_days = models.FloatField(default=0)


class Overtime(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="overtime")
    date = models.DateField()
    workInHour = models.FloatField()  

class Bonus(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="bonus")
    date = models.DateField()
    occation = models.CharField(max_length=250)  
    bonus_price = models.FloatField(default=0)