from django.urls import path
from .views import registerUser, viewProjectsById, viewProjects, updateProjects, updateCompleted, deleteProjects
# from rest_framework.authtoken.views import obtain_auth_token

app_name = 'pywebapi'

urlpatterns = [
    path('register', registerUser, name="uRegister"),
    # path('api/projects/auth', obtain_auth_token),
    path('<projectId>', viewProjectsById, name="proDetails"),
    path('projects', viewProjects, name="AllProjects"),
    path('updateprojects/<projectId>', updateProjects, name="upProjects"),
    path('updateCompleted/<projectId>', updateCompleted, name="upCompleted"),
    path('deleteProjects/<projectId>', deleteProjects, name="delProjects"),
]