from django.db import models
from django.contrib.auth.models import User, AbstractUser
from .validators import validate_file_extension
import datetime
from django.core.validators import FileExtensionValidator


from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings

# Create your models here.

class Jobseeker(AbstractUser):
    # email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    # file = models.ImageField(upload_to="" , null=True)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    # def send_verification_email(self):
    #     subject = 'Verify your email'
    #     message = render_to_string('verification_email.html', {
    #         'user': self,
    #         'uid': urlsafe_base64_encode(force_bytes(self.pk)),
    #         'token': default_token_generator.make_token(self),
    #     })
    #     from_email = settings.DEFAULT_FROM_EMAIL
    #     recipient_list = [self.email]
    #     send_mail(subject, message, from_email, recipient_list)
        
    def __str__(self):
        return str(self.first_name)+"_"+str(self.last_name)+" : "+str(self.email)


class Jobs(models.Model):
    jobname = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    pay = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    application_start_date = models.DateField(null=True)
    application_end_date = models.DateField(null=True)
    # file = models.ImageField(upload_to="" , null=True)
    def __str__(self):
        return self.jobname
    
# class Application(models.Model):
#     name = models.CharField(max_length=100)
#     jobname = models.ForeignKey(Jobs,on_delete=models.CASCADE,null=True)
#     email = models.CharField(max_length=50)
#     phone = models.CharField(max_length=10)
#     desc = models.CharField(max_length=1000)
#     # file = models.FileField()
#     def __str__(self):
#         return self.email
    
class Application(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.SET_NULL, null=True)
    jobseeker = models.ForeignKey(Jobseeker, on_delete=models.SET_NULL, null=True)
    desc = models.CharField(max_length=1000)
    approve = models.BooleanField(default=False)
    file = models.FileField(upload_to="applicant/cv/", validators=[FileExtensionValidator(['pdf'])])
    def __str__(self):
        return self.jobseeker.email
    
    
class Resume(models.Model):
    jobseeker = models.ForeignKey(Jobseeker, on_delete=models.SET_NULL, null=True)
    full_name=models.CharField(max_length=1000,null=True)
    address=models.CharField(max_length=1000,null=True)
    phone=models.CharField(max_length=1000,null=True)
    email=models.EmailField(null=True)
    about_you=models.CharField(max_length=1000,null=True)
    skills = models.CharField(max_length=1000,null=True)
    education=models.CharField(max_length=1000,null=True)
    career=models.CharField(max_length=1000,null=True)
    work_experience=models.CharField(max_length=1000,null=True)
    job_1_start=models.DateField(null=True)
    job_1_end=models.DateField(null=True)
    job_1_details=models.CharField(max_length=1000,null=True)
    references=models.CharField(max_length=1000,null=True)

    def __str__(self):
        return self.full_name