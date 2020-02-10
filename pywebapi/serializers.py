from rest_framework import serializers
from pywebapi.models import Users, Projects, Actions

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'password']
        
    def save(self):
        user = Users(
            username=self.validated_data['username'],
        )
        user.save()
        return user

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'name', 'description', 'completed']
        

class ActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actions
        fields = '__all__'
         