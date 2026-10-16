from django.db import models

# Create your models here.
"""
Schema : QuestionsDb
Field  : title, language, notes, difficulty_level, sample_input, sample_output,
topic, published_date, is_active
"""
class QuestionsDb(models.Model):
    title = models.CharField(max_length=200)
    LANGUAGE_CHOICES = (
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('JavaScript', 'JavaScript')
    )
    language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES)
    DIFFICULTY_CHOICES = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard')
    )
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    topic = models.CharField(max_length=100)
    notes = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    sample_input = models.TextField()
    sample_output = models.TextField()  
    is_active = models.BooleanField(default=True)