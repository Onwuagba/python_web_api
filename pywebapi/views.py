from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from .models import Users, Projects, Actions
from .serializers import UsersSerializer, ProjectsSerializer, ActionsSerializer

@api_view(['POST'])
def registerUser(request):
    if request.method == 'POST':
        create_user = UsersSerializer(data=request.data)
        data = {}
        if create_user.is_valid():
            userDetails = create_user.save()
            data['response'] = "user has been successfully registered."
            data['username'] = userDetails.username
            token = Token.objects.get(user=userDetails).key
            data['token'] = token
        else:
            data = create_user.errors
        return Response(data)


#Retrieve project when id is specified 
@api_view(['GET', ])
def viewProjectsById(request, projectId):
    try:
        project = Projects.objects.get(id=projectId)
        # if isinstance(projectId, int):
        #     project = Projects.objects.get(id=projectId)
        # else:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
    except Projects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    view_project = ProjectsSerializer(project)
    return Response(view_project.data)

#Retrieve all projects
@api_view(['GET', ])
def viewProjects(request):
    try:
        project = Projects.objects.filter()
    except Projects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    view_all_project = ProjectsSerializer(project)
    return Response(view_all_project.data)


#update projects by id
@api_view(['PUT', ])
def updateProjects(request, projectId):
    try:
        project = Projects.objects.get(id=projectId)
    except Projects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        update_project = ProjectsSerializer(project, data=request.data)
        data = {}
        if update_project.is_valid():
            update_project.save()
            data["message"] = "Project updated successfully"
            return Response(data=data)
        return Response(update_project.errors, status=status.HTTP_400_BAD_REQUEST)


#update completed property of project
@api_view(['PATCH', ])
def updateCompleted(request, projectId):
    try:
        project = Projects.objects.get(id=projectId)
    except Projects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PATCH":
        update_project = ProjectsSerializer(project, data=request.data)
        data = {}
        if update_project.is_valid():
            update_project.save()
            data["message"] = "Project updated successfully"
            return Response(data=data)
        return Response(update_project.errors, status=status.HTTP_400_BAD_REQUEST)


#delete projects by ID
@api_view(['DELETE', ])
def deleteProjects(request, projectId):
    try:
        project = Projects.objects.get(id=projectId)
    except Projects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        delete_project = project.delete()
        data = {}
        if delete_project:
            data["message"] = "Project was successfully deleted"
        else:
            data["failure"] = "An error occurred while trying to delete selected project"
            
        return Response(data=data)