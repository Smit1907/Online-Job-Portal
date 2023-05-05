from traceback import print_tb
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.shortcuts import render, get_object_or_404
from datetime import date

# from django.contrib.sites.shortcuts import get_current_site
# from django.urls import reverse
# import random
# import string
# from .utils import *


def index(request): 
    today_date = date.today()
    jobs = Jobs.objects.filter(application_end_date__gte=today_date)
    
    return render(request, "index.html",{'jobs':jobs})

def admin_dashboard(request): 
    if request.user.is_authenticated:
        jobseekers = Jobseeker.objects.all()
        # if request.method == "POST":         
        #     w = Jobseeker.objects.get(id=request.POST['id'])
        #     w.is_active = request.POST['is_active'] == 'True'
        #     w.save()
        #     return redirect('admin_dashboard')


        return render(request, "admin/admin_dashboard.html",{'jobseekers':jobseekers})
    alert = True
    return render(request, "admin/admin_dashboard.html", {'alert':alert})

def admin_side_EditUser(request, myid):
    jobseeker = Jobseeker.objects.filter(id=myid).first()
    if request.method == "POST":
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        is_staff = request.POST.get('is_staff') 
        is_active = request.POST.get('is_active') 
        try:
            print()
            u = Jobseeker.objects.get(id=jobseeker.id)          
            u.username = username
            u.first_name = first_name
            u.last_name = last_name
            u.phone_number = phone_number
            u.email = email
            u.is_staff = is_staff
            u.is_active = is_active
            u.save()
            print("+++++++++++++++++++++++++++++++++++++++++++",u.last_name)
            # return render(request, "admin_side_AddJob.html")
            return redirect('admin_dashboard')
        except:
            pass
    return render(request, "admin/admin_side_EditUser.html",{'jobseeker':jobseeker})


def admin_side_ApplicationsPage(request): 
    if request.user.is_authenticated:
        applications = Application.objects.all()
        jobs = Jobs.objects.all()
        return render(request, "admin/admin_side_ApplicationsPage.html",{'applications':applications,'jobs':jobs})
    alert = True
    return render(request, "admin/admin_side_ApplicationsPage.html", {'alert':alert})

def delete_application(request,myid):
    applications = Application.objects.filter(id = myid)
    applications.delete()
    return redirect('admin_side_ApplicationsPage')

def save_application(request):
    return redirect('admin_side_ApplicationsPage')


def handle_uploaded_job_file(f):  
    with open('media/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk) 

def admin_side_AddJob(request):
    from .validators import validate_file_extension

    jobs = Jobs.objects.all()
    if request.method=="POST":   
            jobname=request.POST['jobname']
            company=request.POST['company']
            description=request.POST['description']
            pay = request.POST['pay']
            address = request.POST['address']
            sdate = request.POST['sdate']
            edate = request.POST['edate']

            if edate<sdate:
                alert = True
                return render(request, "admin/admin_side_AddJob.html", {"alert":alert,'jobs':jobs})

            job = Jobs.objects.create(jobname=jobname,company=company,description=description,pay=pay,address=address,application_start_date=sdate,application_end_date=edate)
            job.save()
            return redirect('admin_side_AddJob')

    return render(request, "admin/admin_side_AddJob.html",{'jobs':jobs})

def admin_side_EditJob(request, myid):
    job = Jobs.objects.filter(id=myid).first()

    if request.method == "POST":
        jobname=request.POST.get('jobname')
        company=request.POST.get('company')
        description = request.POST.get('description')
        pay = request.POST.get('pay')
        address = request.POST.get('address')
        sdate = request.POST.get('sdate')
        edate = request.POST.get('edate')

        if edate<sdate:
            alert = True
            return render(request, "admin/admin_side_EditJob.html", {"alert":alert,'job':job})
        try:
            print()
            u = Jobs.objects.get(id=job.id)          
            u.jobname =jobname
            u.company = company
            u.description = description
            u.pay = pay
            u.address = address
            u.application_start_date = sdate
            u.application_end_date = edate
            u.save()
            print("+++++++++++++++++++++++++++++++++++++++++++",u.jobname)

            return redirect('admin_side_AddJob')
        except:
            pass
    return render(request, "admin/admin_side_EditJob.html",{'job':job})





def delete_job(request,myid):
    jobs = Jobs.objects.filter(id = myid)
    jobs.delete()
    return redirect('admin_side_AddJob')





def admin_side_Applicant(request): 
    if request.user.is_authenticated:
        applications = Application.objects.all()
        return render(request, "admin/admin_side_Applicant.html",{'applications':applications})
    alert = True
    return render(request, "admin/admin_side_Applicant.html", {'alert':alert})

def delete_applicant(request,myid):
    applications = Application.objects.filter(id = myid)
    applications.delete()
    return redirect('admin_side_ApplicationsPage')



def delete_user(reqeest,myid):
    jobseekers = Jobseeker.objects.filter(id = myid)
    jobseekers.delete()
    
    return redirect('admin_dashboard')


def admin(request):
    return redirect("/admin")

def admin_register(request):
    if request.user.is_authenticated:
        return redirect("/admin")
    else:
        if request.method=="POST":   
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            phone_number = request.POST.get('phone_number')
            email = request.POST.get('email')

            if password1 != password2:
                alert = True
                return render(request, "admin_register.html", {'alert':alert})
            
            user = Jobseeker.objects.create_superuser(username=username, password=password1, email=email, first_name = first_name, last_name =last_name,phone_number=phone_number)
            user.save()
            return HttpResponseRedirect("/admin_login/")
    return render(request, "admin_register.html")


# from django.shortcuts import redirect, render
# from django.contrib.auth import get_user_model
# from django.urls import reverse
# from django.utils.http import urlsafe_base64_decode
# from django.contrib.auth.tokens import default_token_generator

# def verify_email(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = get_user_model().objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
#         user = None

#     if user and default_token_generator.check_token(user, token):
#         user.is_verified = True
#         user.save()
#         return redirect(reverse('index')) # Redirect to home page after successful verification
#     else:
#         return render(request, 'verification_failed.html')
    
    
def register(request):
    jobseekers = Jobseeker.objects.all()
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":   
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            username = request.POST.get('username')
            # file = request.FILES.get('file')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            phone_number = request.POST.get('phone_number')
            email = request.POST.get('email')

            if password1 != password2:
                alert = True
                return render(request, "register.html", {'alert':alert})
            
            for jobseeker in jobseekers:
                if jobseeker.email == email:
                    alertForAlreadyExistEmail = True
                    return render(request, "register.html", {'alertForAlreadyExistEmail':alertForAlreadyExistEmail})

            user = Jobseeker.objects.create_user(username=username, password=password1, email=email, first_name = first_name, last_name =last_name,phone_number=phone_number)#,file=file
            user.save()
            # user.send_verification_email()
            
            print("=================",user.email)
            
            # current_site = get_current_site(request).domain
            # relativeLink = reverse('email-verify')

            # random_string = ''.join(random.choices(string.ascii_uppercase + string.digits , k=30))
            # index = random.randint(0, len(random_string))

            # absurl = f'http://{current_site}{relativeLink}?hS23D={random_string[:index]}&tA={user.id}&l2xS={random_string[index:]}'
            # email_body = f'Hi {user.first_name}, use the link below to verify your email:\n{absurl}'
            # data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Verify your email', 'user_id': user.id}
            # Util.send_email(data)

            return HttpResponseRedirect("/login/")
    return render(request, "register.html")



def Login(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request,"you logged in")
                return redirect("/")
            else:
                alert = True
                return render(request, "login.html", {"alert":alert})
    return render(request, "login.html")

def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user.is_superuser:
            login(request, user)
            messages.success(request,"you logged in")
            return redirect("/admin_dashboard")
        else:
            alert = True
            return render(request, "admin_login.html", {"alert":alert})
    return render(request, "admin_login.html")

def Logout(request):
    logout(request)
    messages.success(request,"you logged out")
    return HttpResponseRedirect("/")










def job_view(request, myid):
    job = Jobs.objects.filter(id=myid).first()

    if request.method=="POST":
        content = request.POST['content']
        return render(request,f"/job_view/{job.id}")
    return render(request, "job_view.html", {'job':job})
 
def handle_uploaded_CV(f):  
    with open('app/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk) 

def application(request,pk,myid):
    jobs = Jobs.objects.filter(id=pk).first()
    jobseeker = Jobseeker.objects.filter(id=myid).first()
    if request.method=="POST": 
        job = get_object_or_404(Jobs, pk=pk)
        name = request.POST['name']
        jobseeker = jobseeker
        desc = request.POST['desc']
        jobname = job
        file = request.FILES['file']

        application = Application(jobseeker=jobseeker,job = jobname,desc=desc,file=file) 
        application.save()
        messages.success(request,"your application is sent")
        return HttpResponseRedirect("/")
    return render(request, "application.html",{'job':jobs,'jobseeker':jobseeker}) 

def applied_jobs(request):
    applied_jobs = Application.objects.all()
    return render(request, "applied_jobs.html",{'applied_jobs':applied_jobs})

def create_resume(request,myid): 
    jobseeker = Jobseeker.objects.filter(id=myid).first()
    if request.method=="POST":
        work_experience=request.POST.get("work_experience")
        if work_experience == "fresher":
            jobseeker = jobseeker
            full_name=request.POST.get("name")
            address=request.POST.get("address")
            phone=request.POST.get("phone")
            email=request.POST.get("email")
            about_you=request.POST.get("about")
            skills=request.POST.get("skills")
            education=request.POST.get("education")
            career=request.POST.get("career")
            work_experience=request.POST.get("work_experience")
            references=request.POST.get("references")

            resume = Resume.objects.create(jobseeker = jobseeker,full_name=full_name,address=address,phone=phone,email=email,about_you=about_you,skills=skills,education=education,career=career,work_experience=work_experience,references=references)
            resume.save()
            return redirect('resume')
        else:
            jobseeker = jobseeker
            full_name=request.POST.get("name")
            address=request.POST.get("address")
            phone=request.POST.get("phone")
            email=request.POST.get("email")
            about_you=request.POST.get("about")
            skills=request.POST.get("skills")
            education=request.POST.get("education")
            career=request.POST.get("career")
            work_experience=request.POST.get("work_experience")
            job_1_start=request.POST.get("job-1__start")
            job_1_end=request.POST.get("job-1__end")
            job_1_details=request.POST.get("job-1__details")
            references=request.POST.get("references")

            resume = Resume.objects.create(jobseeker = jobseeker,full_name=full_name,address=address,phone=phone,email=email,about_you=about_you,skills=skills,education=education,career=career,work_experience=work_experience,job_1_details=job_1_details,job_1_start=job_1_start,job_1_end=job_1_end,references=references)
            resume.save()
            return redirect('resume')
    return render(request, "create-resume.html")

def resume(request): 
    user_resume = Resume.objects.all()
    return render(request, "resume.html",{'user_resume':user_resume})

def edit_resume(request,myid): 
    jobseeker = Jobseeker.objects.filter(id=myid).first()
    resume = Resume.objects.get(jobseeker=jobseeker)
    today = datetime.date.today()
    if request.method=="POST":
        work_experience=request.POST.get("work_experience")
        print("===========",work_experience)
        if work_experience == "fresher":
            jobseeker = jobseeker
            full_name=request.POST.get("name")
            address=request.POST.get("address")
            phone=request.POST.get("phone")
            email=request.POST.get("email")
            about_you=request.POST.get("about")
            skills=request.POST.get("skills")
            education=request.POST.get("education")
            career=request.POST.get("career")
            references=request.POST.get("references")
            s=Resume.objects.get(id=resume.id)
            s.jobseeker=jobseeker
            s.full_name=full_name
            s.address=address
            s.phone=phone
            s.email=email
            s.about_you=about_you
            s.skills=skills
            s.education=education
            s.career=career
            s.work_experience=work_experience
            s.job_1_start = today
            s.job_1_end = today
            s.job_1_details = "FRESHER"
            s.references=references            
            s.save()
            return redirect('resume')
        else:
            jobseeker = jobseeker
            full_name=request.POST.get("name")
            address=request.POST.get("address")
            phone=request.POST.get("phone")
            email=request.POST.get("email")
            about_you=request.POST.get("about")
            skills=request.POST.get("skills")
            education=request.POST.get("education")
            career=request.POST.get("career")
            work_experience=request.POST.get("work_experience")
            job_1_start=request.POST.get("job-1__start")
            job_1_end=request.POST.get("job-1__end")
            job_1_details=request.POST.get("job-1__details")
            references=request.POST.get("references")

            s=Resume.objects.get(id=resume.id)
            s.jobseeker=jobseeker
            s.full_name=full_name
            s.address=address
            s.phone=phone
            s.email=email
            s.about_you=about_you
            s.skills=skills
            s.education=education
            s.career=career
            s.work_experience=work_experience
            s.job_1_details=job_1_details
            s.job_1_start=job_1_start
            s.job_1_end=job_1_end
            s.references=references            
            s.save()
            return redirect('resume')

    
    return render(request, "edit-resume.html",{'resume_info':resume})


def app_dropdown(request):
    jobs = Jobs.objects.all()
    context = {

        'job' : jobs
    }
    return render(request, "application.html",context)


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == "POST":
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        print("====================........................",current_password)
        print("====================........................",new_password)
        try:
            u = Jobseeker.objects.get(id=request.user.id)
            if u.check_password(current_password):
                u.set_password(new_password)
                u.save()
                alert = True
                return render(request, "change_password.html", {'alert':alert})
            else:
                currpasswrong = True
                return render(request, "change_password.html", {'currpasswrong':currpasswrong})
        except:
            pass
    return render(request, "change_password.html")


def profile(request):	
    if request.method == "POST":	
        first_name=request.POST.get('first_name')	
        last_name=request.POST.get('last_name')	
        phone_number = request.POST.get('phone_number')	
        email = request.POST.get('email')	
        u = Jobseeker.objects.get(id=request.user.id)	
        u.first_name =first_name	
        u.last_name = last_name	
        u.phone_number = phone_number	
        u.email = email	
        u.save()	
        messages.success(request,"your profile has been updated!")	
        return HttpResponseRedirect("/")  	
    return render(request, "profile.html")
