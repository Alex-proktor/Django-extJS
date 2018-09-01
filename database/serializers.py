from rest_framework import serializers
from database.models import Recourse


class RecourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recourse
        fields = ('id', 'operator', 'email', 'phone', 'status', 'text', 'comment')
