from rest_framework import serializers
from traits.serializers import TraitSerializer
from groups.serializers import GroupSerializer


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        ["Male", "Female", "Not Informed"], default="Not Informed"
    )
    group = GroupSerializer(many=False)
    traits = TraitSerializer(many=True)
