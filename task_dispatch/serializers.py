from rest_framework import serializers
from .controller.trello.interest import Interest


class InterestSerializer(serializers.Serializer):
    # key = serializers.IntegerField(read_only=True)
    # key = serializers.(read_only=True)
    key = serializers.CharField(required=False, allow_blank=True, max_length=100)
    img = serializers.CharField(required=False, allow_blank=True, max_length=100)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    value = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        instance = Interest()
        instance.key = validated_data.get('key',instance.key)
        instance.img = validated_data.get('img',instance.key)
        instance.name = validated_data.get('name',instance.key)
        instance.value = validated_data.get('value',instance.key)

        return instance

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.key = validated_data.get('key',instance.key)
        instance.img = validated_data.get('img',instance.key)
        instance.name = validated_data.get('name',instance.key)
        instance.value = validated_data.get('value',instance.key)
        return instance