from mimetypes import MimeTypes
from multiprocessing import context
from django.forms import PasswordInput
from django.shortcuts import render
from .import models
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import auth
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import uuid
# Create your views here.
@csrf_exempt
def home(request):
    try:
        context = {}
        if request.user.is_authenticated:
            return render(request,'home.html',context=context)
        else:
            return redirect('login')
    except Exception as e:
        context = {'exception':e}
        return  render(request,"exception.html",context=context)

@csrf_exempt
def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        context = {}
        if request.POST:
            data = request.POST
            if 'formsubmit' in data:        
                username = data.get('uname')
                Password = data.get('psw')
                user = auth.authenticate(username=username, password=Password)
                print(user)
                if user is not None:
                    auth.login(request,user)
                    return redirect('/')
                else:
                    context.update({
                        'user_status':"False"
                    })
        
        return render(request,'login.html',context=context)

@csrf_exempt
def logout(request):
    auth.logout(request)
    return redirect('/')


@csrf_exempt
def donation(request):
    return render(request,'donation.html')

@csrf_exempt
def report(request):
    return render(request,'report.html')
    

@csrf_exempt
def aboutus(request):
    return render(request,'aboutus.html')

@csrf_exempt
def logaboutus(request):
    return render(request,'logaboutus.html')


def signup(request):
    # send_email()
    context={}
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.POST:
            data = request.POST
            if 'signupsubmit' in data:
                first_name = request.POST.get('firstname')
                last_name = request.POST.get('lastname')
                
                email = request.POST.get('email')
                mobileno = request.POST.get('mobileno')
                
                password = request.POST.get('psw')
                # password1 =request.POST.get('psw1')
            
                obj,created = models.UserAccounts.objects.get_or_create(
                    username = email,
                    email = email,
                    first_name = first_name,
                    last_name = last_name
                )

                if created:
                    # send_email(email)
                    obj.mobile_number = mobileno 
                    obj.set_password(password)
                    obj.save()
        # if request.POST:
        #      data = models.Report.objects.all()

                return redirect('login')

            
    return render(request,'signup.html',context=context)


# def send_email(toaddr):
#     # try:
#     fromaddr = "rahul.ramachandran@science.christuniversity.in"
#     toaddr = toaddr
#     password="90891399"
#     msg = MIMEMultipart()
#     msg['From'] = fromaddr
#     msg['To'] = toaddr
#     msg['Subject'] = "Test Mail"
#     body = " This is a test mail to check smtp mail library"
#     msg.attach(MIMEText(body,"plain"))
#     s = smtplib.SMTP('smtp.gmail.com', 587)
#     print(s)
#     s.starttls()
#     s.login(fromaddr, password)

#     text = msg.as_string()
#     print(text)
#     s.sendmail(fromaddr, toaddr, text)
#     s.quit()
