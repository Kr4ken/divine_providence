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
    key = serializers.CharField(required=True,max_length=30)
    list_key = serializers.CharField(required=True,max_length=30)
    # task_type = serializers.ForeignKey(Task_type)
    # urgency = serializers.ForeignKey(Urgency)
    name = serializers.CharField(required=True,max_length=100)
    description = serializers.CharField(required=False,max_length=2000)
    special = serializers.CharField(required=False,max_length=300)
    # type = serializers.ForeignKey(Type)
    due_date=serializers.DateField(required=False)
    checklist=serializers.CharField(required=False,max_length=200)
    labels=serializers.CharField(required=False,max_length=200)
    sub_task=serializers.CharField(required=False,max_length=40)
    atribute=serializers.CharField(required=False,max_length=10)
    difficult=serializers.CharField(required=False,max_length=10)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        instance = Task
        instance.key = validated_data.get('key',instance.key)
        instance.list_key = validated_data.get('list_key',instance.list_key)
        # instance.task_type = validated_data.get('task_type',instance.task_type)
        # instance.urgency = validated_data.get('urgency',instance.urgency)
        instance.name = validated_data.get('name',instance.name)
        instance.description =validated_data.get('description',instance.description)
        instance.special = validated_data.get('special',instance.special)
        # instance.type = validated_data.get('type',instance.type)
        instance.due_date=validated_data.get('due_date',instance.due_date)
        instance.checklist=validated_data.get('checklist',instance.checklist)
        instance.labels=validated_data.get('labels',instance.labels)
        instance.sub_task=validated_data.get('sub_task',instance.sub_task)
        instance.atribute=validated_data.get('atribute',instance.atribute)
        instance.difficult=validated_data.get('difficult',instance.difficult)
        return instance

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.key = validated_data.get('key',instance.key)
        instance.list_key = validated_data.get('list_key',instance.list_key)
        # instance.task_type = validated_data.get('task_type',instance.task_type)
        # instance.urgency = validated_data.get('urgency',instance.urgency)
        instance.name = validated_data.get('name',instance.name)
        instance.description =validated_data.get('description',instance.description)
        instance.special = validated_data.get('special',instance.special)
        # instance.type = validated_data.get('type',instance.type)
        instance.due_date=validated_data.get('due_date',instance.due_date)
        instance.checklist=validated_data.get('checklist',instance.checklist)
        instance.labels=validated_data.get('labels',instance.labels)
        instance.sub_task=validated_data.get('sub_task',instance.sub_task)
        instance.atribute=validated_data.get('atribute',instance.atribute)
        instance.difficult=validated_data.get('difficult',instance.difficult)
        return instance

