from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


# Create a UserUpdateForm to update a username and email
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Jobseeker
        fields = "__all__"

class UploadfileForms(forms.Form):
    file = forms.FileField()



# Create a ProfileUpdateForm to update image.
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Jobseeker   
#         fields = ['phone_number']