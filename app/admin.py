from django.contrib import admin
from . models import *
from .forms import *
from django.contrib.auth.admin import UserAdmin

# admin.site.register(Jobseeker)
admin.site.register(Jobs)
admin.site.register(Application)
admin.site.register(Resume)

# Register your models here.

class CustomeUserAdmin(UserAdmin):
    model = Jobseeker
    add_from = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (None, {
            "fields": (
                'phone_number','is_verified',

            ),
        }),
    )
    


admin.site.register(Jobseeker,CustomeUserAdmin)