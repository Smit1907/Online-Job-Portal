from django import views
from django.urls import path,include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("create_resume/<int:myid>/", views.create_resume, name="create_resume"),
    path("resume/", views.resume, name="resume"),
    path("edit_resume/<int:myid>/", views.edit_resume, name="edit_resume"),
    
    path("register/", views.register, name="register"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
    path("job_view/<int:myid>/", views.job_view, name="job_view"),
    path("applied_jobs/", views.applied_jobs, name="applied_jobs"),
    path("application/<int:pk>/<int:myid>/", views.application, name="application"),
    path("change_password/", views.change_password, name="change_password"),
    path("profile/", views.profile, name="profile"),
    # path('verify-email/<str:uidb64>/<str:token>/', views.verify_email, name='verify_email'),


# admin admin admin admin admin admin admin admin admin admin admin admin admin admin admin admin admin admin admin admin 


    path("admin_login/", views.admin_login, name="admin_login"),
    path("delete_user/<int:myid>/", views.delete_user, name="delete_user"),
    path("delete_application/<int:myid>/", views.delete_application, name="delete_application"),
    path("delete_job/<int:myid>/", views.delete_job, name="delete_job"),
    # path("save_application/", views.save_application, name="save_application"),
    path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("admin_side_ApplicationsPage/", views.admin_side_ApplicationsPage, name="admin_side_ApplicationsPage"),
    path("admin_side_Applicant/", views.admin_side_Applicant, name="admin_side_Applicant"),
    path("admin_register/", views.admin_register, name="admin_register"),
    path("admin_side_AddJob/", views.admin_side_AddJob, name="admin_side_AddJob"),
    path("admin_side_EditJob/<int:myid>/", views.admin_side_EditJob, name="admin_side_EditJob"),
    path("admin_side_EditUser/<int:myid>/", views.admin_side_EditUser, name="admin_side_EditUser"),
    path("admin/", views.admin, name="admin"),
]
