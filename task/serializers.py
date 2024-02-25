from rest_framework import serializers
from rest_framework.exceptions import ValidationError


from .models import Task

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__al__'



