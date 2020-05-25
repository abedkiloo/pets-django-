from rest_framework import serializers

from .models import Puppies


class PuppySerializer(serializers.ModelSerializer):
    class Meta:
        model = Puppies
        fields = ('name', 'age', 'breed', 'color', 'created_at', 'update_at')
