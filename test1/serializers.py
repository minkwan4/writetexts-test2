from rest_framework import serializers
from .models import Writetext

class WritetextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writetext
        fields = ('title', 'maintext', 'datetime')