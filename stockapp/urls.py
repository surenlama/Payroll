from django.urls import path
from .import views


urlpatterns = [
    path('', views.home,name="home"),
    path('signup/', views.signup,name="signup"),
    path('signin/', views.signin,name="signin"),
    path('viewprofile/', views.viewprofile,name="viewprofile"),
    path('updateprofile/', views.updateprofile,name="updateprofile"),
    path('changepassword/', views.changepass,name="changepass"),
    path('contactus/', views.contactus,name="contactus"),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('service/', views.service,name="service"),
    path('sendemail/', views.sendemail,name="sendemail"),
    path('logouts/', views.logouts,name="logouts"),
    path('employee/', views.Employees,name="employee"),
    path('aboutus/', views.aboutus,name="aboutus"),
    path('attendence/', views.attendance,name="attendence"),
    # path('list/attendence/', views.attendenceshow,name="attendenceshow"),
    path('totalsalary/', views.totalsalaries,name="totalsalary"),


]
