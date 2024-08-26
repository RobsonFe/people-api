from rest_framework import serializers

from people.models.entity.people_models import People


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = "__all__"
