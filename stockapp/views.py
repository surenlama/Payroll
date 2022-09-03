from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import  Bonus, Category, Overtime,Register,Attendance
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Contact,Employee
from django.core.mail import EmailMessage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView
from .forms import EmployeeCreationForm,AttendenceCreationForm,OvertimeCreationForm,BonusCreationForm

def home(request):
    return render(request,'home.html')

def signup(request):
    msg=""
    if request.method=="POST":
        fname=request.POST['fname']
        passw=request.POST['passw']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        contact=request.POST['contact']
        age=request.POST['age']
        gender=request.POST['gender']  
        occu=request.POST['occupation']   
        utype=request.POST['utype']
        a=User.objects.filter(username=uname)
        if a:
            msg="User already exists"    
        else:
            us=User.objects.create_user(username=uname,email=email,password=passw)  
            us.first_name=fname
            us.last_name=lname
            us.username=uname
            us.email=email

            if "a" in utype:
                us.is_active=True
                us.is_staff=True
                us.is_superuser=True

            if "d" in utype:
                us.is_staff=True

            if "p" in utype:
                us.is_active=True 

            us.save()
            r=Register(user=us,contact_number=contact,age=age,gender=gender,occupation=occu)
            r.save()
            if "image" in request.FILES:
                img=request.FILES['image']
                r.profile=img
                r.save()
                msg="Sucessfully register"    
        return render(request,'signup.html',{'msg':msg})    
    return render(request,'signup.html')

def signin(request):
    if request.method=="POST":
        uname=request.POST['uname']
        passw=request.POST['passw']

        a=authenticate(username=uname,password=passw)
        if a:
            login(request,a)
            if a.is_superuser:
                return redirect('http://127.0.0.1:8000/admin')
            if a.is_staff:
                return redirect(dashboard)
            if a.is_active:
                return redirect(dashboard)
        else:
            msg="Invalid credintial"        
            return render(request,'signin.html',{'msg':msg})          
    return render(request,'signin.html')    


def viewprofile(request):
    a=Register.objects.filter(user__id=request.user.id)
    if a:
        r=Register.objects.get(user__id=request.user.id)
        return render(request,'viewprofile.html',{'data':r})       
    else:
        msg="No data"
        return render(request,'viewprofile.html',{'msg':msg})          
    return render(request,'viewprofile.html')    

def updateprofile(request):
    msg=""
    a=Register.objects.filter(user__id=request.user.id)
    if a:
        r=Register.objects.get(user__id=request.user.id)
        if request.method=='POST':
            fname=request.POST['fname']
            lname=request.POST['lname']
            uname=request.POST['uname']
            email=request.POST['email']
            contact=request.POST['contact']
            age=request.POST['age']
            gender=request.POST['gender']
            occupation=request.POST['occupation']
            usr=User.objects.get(id=request.user.id)
            usr.first_name=fname
            usr.last_name=lname
            usr.username=uname
            usr.email=email
            usr.save()
            r.user=usr
            r.contact_number=contact
            r.age=age
            r.gender=gender
            r.occupation=occupation
        
            if "image" in request.FILES:
                img=request.FILES['image']
                r.profile=img           
                msg="Sucessfully register"
            r.save()    
        return render(request,'updateprofile.html',{'data':r,'msg':msg}) 
    else:
        msg="No data"
        return render(request,'updateprofile.html',{'msg':msg})       
    return render(request,'updateprofile.html')    

def changepass(request):
    if request.method=="POST":
        current=request.POST['currentpass']
        change=request.POST['changepass']
        confirm=request.POST['confirmpass']
        usr=User.objects.get(id=request.user.id)
        b=usr.username
        v=usr.check_password(current)
        if v:
            if change==confirm:               
                usr.set_password(confirm)
                usr.save()
                us=User.objects.get(username=b)
                login(request,us)
                msg="Sucessfully changed password"
            else:
                msg="Password doesn't match"    
        else: 
            msg="Incorrect current password"   
        return render(request,'changepass.html',{'msg':msg})
    return render(request,'changepass.html')


def contactus(request):
    contact_check=Contact.objects.all()[:5]
    if request.method=="POST":
        name = request.POST['name']
        contact_number = request.POST['number']
        subject = request.POST['subject']
        message = request.POST['message']
        contact=Contact(name=name,number=contact_number,subject=subject,message=message)
        contact.save()
        msg="Sucessfully Contact saved"
        return render(request,'contactus.html',{'data':msg})

    return render(request,'contactus.html',{'Contactdata':contact_check})    

def dashboard(request):
    return render(request,'cust.html')

def service(request):
    return render(request,'service.html')    

def sendemail(request):
    if request.user.is_authenticated:
        data=""
        if request.method=="POST":
            rec=request.POST['to']
            subject=request.POST['subject']
            message=request.POST['message']
            try:
                em=EmailMessage(subject,message,to=[rec])
                em.send()
                data="Email sent"
                return render(request,'sendemail.html',{"data":data})
            except:
                data="Could not sent please check internet connection/Email address"
        return render(request,'sendemail.html',{"data":data})
    return render(request,'sendemail.html',{"data":"Login first"})

def logouts(request):
    logout(request)
    return render(request,'base.html')


class EmployeeCreateView(LoginRequiredMixin,CreateView):
    form_class = EmployeeCreationForm
    template_name = "employee.html"
    success_url = '/employee/'


class EmployeeList(LoginRequiredMixin,ListView):
    model = Employee
    template_name = "employeelist.html"
    success_url = '/employeelist/'
    context_object_name = "employee_list"


def aboutus(request):
    return render(request,'aboutus.html')


class AttendenceCreateView(LoginRequiredMixin,CreateView):
    form_class = AttendenceCreationForm
    template_name = "attendance.html"
    success_url = '/attendence/'

def attendenceshow(request):
    attendenceobject = Attendance.objects.filter(status="Absent")
    return render(request,'showattendence.html',{'attendence':attendenceobject})


def totalsalaries(request):
    data = ""
    employeeobject = Employee.objects.all()
    for i in employeeobject:

        rec=i.email
        print(i.email)
        subject="Monthly salary payment"
        message=f"You account has been sucessfully credited by {i.salary} and becames {i.bankamount}"
        em=EmailMessage(subject,message,to=[rec,])
        em.send()
        data="Email sent"
    return render(request,'totalsalary.html',{"msg":"please check your mail for your salary info",'salary':employeeobject})
        # except:
        #     data="Could not sent please check internet connection/Email address"
        #     return render(request,'totalsalary.html',{"data":data,'salary':employeeobject})
    return render(request,'totalsalary.html',{"data":data,'salary':employeeobject})

class AttendenceCreateView(LoginRequiredMixin,CreateView):
    form_class = AttendenceCreationForm
    template_name = "attendance.html"
    success_url = '/attendence/'



class OvertimeCreateView(LoginRequiredMixin,CreateView):
    form_class = OvertimeCreationForm
    template_name = "overtime.html"
    success_url = '/overtime/'


class OvertimeList(LoginRequiredMixin,ListView):
    model = Overtime
    template_name = "overtimelist.html"
    success_url = '/list/overtime/'
    context_object_name = "overtime_list"

class BonusCreateView(LoginRequiredMixin,CreateView):
    form_class = BonusCreationForm
    template_name = "bonus.html"
    success_url = '/bonus/'

