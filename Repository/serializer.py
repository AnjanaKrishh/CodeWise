from rest_framework import serializers
from Repository.models import QuestionsDb

class QuestionsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    language = serializers.ChoiceField(choices=QuestionsDb.LANGUAGE_CHOICES,default="python")
    difficulty_level = serializers.ChoiceField(choices=QuestionsDb.DIFFICULTY_CHOICES,default="easy")
    topic = serializers.CharField(max_length=100)
    notes = serializers.CharField(max_length=200)
    published_date = serializers.DateTimeField(read_only=True)
    sample_input = serializers.CharField(max_length=1000)
    sample_output = serializers.CharField(max_length=1000)
    is_active = serializers.BooleanField(default=True)

    