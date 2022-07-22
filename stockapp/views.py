from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import  Category,Register,Attendance
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from .models import Contact,Employee
from django.core.mail import EmailMessage


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
    contact_check=Contact.objects.all()
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
    data=""
    register=Register.objects.filter(user__id=request.user.id)
    if register:
        register=Register.objects.get(user__id=request.user.id)
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
    else:
        return render(request,'sendemail.html',{'data':"Sorry you don't have data"})    
    return render(request,'sendemail.html')    

def logouts(request):
    logout(request)
    return render(request,'base.html')

def Employees(request):
    if request.method=="POST":
        attendence=request.POST['attendence']
        status=request.POST['status']
          
        employee_object=Employee(name=request.POST['name'],phone=request.POST['phone'],\
        email=request.POST['email'],tax=request.POST['tax'],salary=request.POST['salary'],\
            join=request.POST['join'])   
        employee_object.save()
        if "present " in attendence:
            employee_object.attendence="present"
        if "absent" in attendence :
            employee_object.attendence="present"
        if "partial" in attendence:
            employee_object.attendence="partial"

        if "part " in status:
            employee_object.work="part"
        if "over" in status :
            employee_object.work="over"
        if "normal" in status:
            employee_object.work="normal"       
        employee_object.save()

        msz="Sucessfully Saved Employee"
        return render(request,'employee.html',{'msz':msz})    

    else:    
        return render(request,'employee.html')    
    return render(request,'employee.html')    


def aboutus(request):
    return render(request,'aboutus.html')


def attendance(request):
    if request.method=="POST":
        attendence=request.POST['attendence']
        dates = request.POST['date']
        days = request.POST['day']
        user_object = User.objects.get(id=request.user.id)
        attendence_object = Attendance.objects.create(user=user_object)
        if "present " in attendence:
            attendence_object.status="Present"
        if "absent" in attendence :
            attendence_object.status="Absent"
        if "partial" in attendence:
            attendence_object.status="Partially"
        attendence_object.date = dates 
        attendence_object.no_of_leave_day = days   
        attendence_object.save()    
        return render(request,'attendance.html',{'msg':'Sucessfully recorded'})
    return render(request,'attendance.html')


# def attendenceshow(request):
#     attendenceobject = Attendance.objects.filter(user=request.user)
#     print(attendenceobject)
#     return render(request,'showattendence.html',{'attendence':attendenceobject})


def totalsalaries(request):
    employeeobject = Employee.objects.all()
    return render(request,'totalsalary.html',{'salary':employeeobject})    