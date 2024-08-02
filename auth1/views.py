from django.shortcuts import render,redirect
from redirection.models import Users_main
from django.contrib import messages
from dotenv import load_dotenv
import os
import random
from .models import otps
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from django.utils import timezone
from datetime import timedelta

# Create your views here.

def validate(request):
    if request.method=="POST":
        otp1=request.POST.get('o1')
        otp2=request.POST.get('o2')
        otp3=request.POST.get('o3')
        otp4=request.POST.get('o4')
        otp5=request.POST.get('o5')
        otp6=request.POST.get('o6')

        fianlotp=otp1+otp2+otp3+otp4+otp5+otp6
        email=request.session.get('email12')
        if not request.session.get('email12'):
            messages.error(request,'Session Expired')
            return redirect('/auth/login/')
        try:
            user=otps.objects.get(email=email,expires_at__gt=timezone.now())
            # print(user.otp)
            # print(otp)
            # print(email)
            if user.otp==int(fianlotp) and not user.is_expired():

                if Users_main.objects.get(email=email).is_active== True:
                    context={

                    }

                    response=redirect('/',context) 
                    response.set_cookie('time', 'true', max_age=15*24*60*60)
                    response.set_cookie('email', email, max_age=15*24*60*60)
                    response.set_cookie('Logged_in', 'true', max_age=15*24*60*60)

                    # print("cookie set")
                    try:
                        users12=Users_main.objects.get(email=email)
                    except Users_main.DoesNotExist:
                        messages.error(request,'User not found')
                        return redirect('/auth/login/')
                    request.session['email']=users12.email
                    request.session['unique_link']=users12.unique_link
                    request.session['github_username']=users12.github_username
               
                    
                    user.delete()
                    return response
                
                else:
                    user.delete()
                    return response
            else:
                messages.error(request, 'Invalid OTP')
                return render(request, 'OTP.html')
            
        except otps.DoesNotExist:
            messages.error(request,"OTP Expired")
            return redirect('/auth/login')
        

    return render(request, 'OTP.html')


def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            user=Users_main.objects.get(email=email)
        except Users_main.DoesNotExist:
            messages.error(request,'User not found')
            return redirect('/auth/login/')
        
        if not user.is_active:
            messages.error(request,'Some Unusual Activity Detected on your account so we have disabled your account, Please contact support')
            return redirect('/auth/login/')

        islogin=user.check_password(password)
        if user.email==email and islogin:
            request.session['email']=user.email
            request.session['unique_link']=user.unique_link
            request.session['github_username']=user.github_username
            if  request.COOKIES.get('time') and request.COOKIES.get('email')==user.email:
                context={

                    }

                response=redirect( '/',context) 
                response.set_cookie('time', 'true', max_age=15*24*60*60)
                response.set_cookie('email', email, max_age=15*24*60*60)
                response.set_cookie('Logged_in', 'true', max_age=15*24*60*60)

                return response
            
            load_dotenv()
            from_email=os.getenv('EMAIL12')
            password=os.getenv('PASSWORD12')

            request.session['email12']=email
            subject="One Time Password For Login "
            length=8
            otp=random.randint(111111,999999)
            body=f"""

                <div style="font-family: Arial, sans-serif; color: #333;">
            <h1 style="text-align: center; color: #4CAF50;">One-Time Password for Secure Login</h1>

            <p>Dear User,</p>

            <p>
                We are thrilled to welcome you back to our platform! It has been over 15 days since your last login, and for your security, we need to verify your device.
            </p>

            <p>
                To proceed with the login process, please use the One-Time Password (OTP) provided below. This OTP is unique to your login attempt and will expire in 10 minutes for security purposes.
            </p>

            <div style="text-align: center; margin: 20px 0;">
                <h2 style="display: inline-block; background: #f4f4f4; padding: 10px 20px; border: 1px solid #ddd; border-radius: 5px;">{otp}</h2>
            </div>

            <p>
                Enter this OTP on the login page to verify your identity and continue accessing your account.
            </p>

            <p>
             If you did not request this login, please ignore this message. No further action is required.
            </p>

            <p>
            Should you have any questions or need assistance, please feel free to contact our team.
            </p>

         <p>
            Thank you for choosing Any Time Event. We are committed to ensuring the security and privacy of your account.
            </p>

            <p>
            Best regards,<br>
            <strong>Github Visitor Analytics tem</strong>
            </p>
            </div>

            """
            msg = MIMEMultipart()
            msg['Subject'] = subject
            msg['From'] = from_email
            msg['To'] = email
            msg.attach(MIMEText(body, 'html'))
            expiry_duration = timedelta(minutes=5)  # Set OTP validity duration
            expires_at = timezone.now() + expiry_duration
            user1=otps(email=email,otp=otp, expires_at=expires_at)
            user1.save()
            print(user1.otp)
                

            print(True)
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(from_email, password)
                server.sendmail(from_email, email, msg.as_string())
                print("OTP Send Successfully")

                print("mail sent")
                        
                    # messages.success(request, 'OTP sent to your email')
                return redirect('/auth/validate')


        
        
    return render(request,'login.html')