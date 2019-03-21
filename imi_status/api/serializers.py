from rest_framework import serializers
from imi_status.models import ImiStatus
from accounts.api.serializers import UserDisplaySerializer

class ImiModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    class Meta:
        model = ImiStatus
        fields = [
            'user',
            'content',
            
        ]