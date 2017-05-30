from rest_framework import serializers
from .controller.trello.interest import Interest


class InterestSerializer(serializers.Serializer):
    # key = serializers.IntegerField(read_only=True)
    # key = serializers.(read_only=True)
    key = serializers.CharField(required=False, allow_blank=True, max_length=100)
    img = serializers.CharField(required=False, allow_blank=True, max_length=100)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    value = serializers.CharField(required=False, allow_blank=True, max_length=100)
    description = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        instance = Interest
        instance.key = validated_data.get('key',instance.key)
        instance.img = validated_data.get('img',instance.img)
        instance.name = validated_data.get('name',instance.name)
        instance.value = validated_data.get('value',instance.value)
        instance.description = validated_data.get('description',instance.description)

        return instance

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.key = validated_data.get('key',instance.key)
        instance.img = validated_data.get('img',instance.img)
        instance.name = validated_data.get('name',instance.name)
        instance.value = validated_data.get('value',instance.value)
        instance.description = validated_data.get('description',instance.description)
        return instance