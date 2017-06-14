from rest_framework import serializers
# from .controller.trello.interest import Interest
from .models import Interest,Task


class InterestSerializer(serializers.Serializer):
    # key = serializers.IntegerField(read_only=True)
    # key = serializers.(read_only=True)
    key = serializers.CharField(required=False, allow_blank=True, max_length=100)
    img = serializers.CharField(required=False, allow_blank=True, max_length=100)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    list_key = serializers.CharField(required=False, allow_blank=True, max_length=100)
    list_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    description = serializers.CharField(required=False, allow_blank=True, max_length=100)
    ord_pos = serializers.IntegerField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        instance = Interest
        instance.key = validated_data.get('key',instance.key)
        instance.img = validated_data.get('img',instance.img)
        instance.name = validated_data.get('name',instance.name)
        instance.list_key = validated_data.get('list_key',instance.list_key)
        instance.list_name = validated_data.get('list_name',instance.list_key)
        instance.description = validated_data.get('description',instance.description)
        instance.ord_pos = validated_data.get('ord_pos',instance.description)

        return instance

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.key = validated_data.get('key',instance.key)
        instance.img = validated_data.get('img',instance.img)
        instance.name = validated_data.get('name',instance.name)
        instance.value = validated_data.get('value',instance.value)
        instance.list_key = validated_data.get('list_key',instance.list_key)
        instance.list_name = validated_data.get('list_name',instance.list_key)
        instance.description = validated_data.get('description',instance.description)
        instance.ord_pos = validated_data.get('ord_pos',instance.description)
        return instance


class TaskSerializer(serializers.Serializer):

    key = serializers.CharField(required=True, max_length=30)
    name = serializers.CharField(required=True, max_length=100)
    description = serializers.CharField(required=False, max_length=500)
    duration = serializers.IntegerField(required=False)
    list_key = serializers.CharField(required=True, max_length=30)
    checklist = serializers.CharField(required=False, max_length=5000)
    due_date = serializers.DateField(required=False)
    attribute = serializers.CharField(required=False, max_length=1)
    labels = serializers.CharField(required=False, max_length=2)
    special = serializers.CharField(required=False, max_length=1000)
    image = serializers.CharField(required=False, max_length=1000)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        instance = Task
        instance.key = validated_data.get('key', instance.key)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.list_key = validated_data.get('list_key', instance.list_key)
        instance.checklist = validated_data.get('checklist', instance.checklist)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.attribute = validated_data.get('attribute', instance.attribute)
        instance.labels = validated_data.get('labels', instance.labels)
        instance.special = validated_data.get('special', instance.special)
        instance.image = validated_data.get('image', instance.image)
        return instance

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.key = validated_data.get('key', instance.key)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.list_key = validated_data.get('list_key', instance.list_key)
        instance.checklist = validated_data.get('checklist', instance.checklist)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.attribute = validated_data.get('attribute', instance.attribute)
        instance.labels = validated_data.get('labels', instance.labels)
        instance.special = validated_data.get('special', instance.special)
        instance.image = validated_data.get('image', instance.image)
        return instance

