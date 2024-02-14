from django.contrib import admin
from .models import ScentOption, Question, QuizQuestion


@admin.register(ScentOption)
class ScentOptionAdmin(admin.ModelAdmin):
    list_display = ('text', 'scent_profile')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text',)

@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('question',)
    filter_horizontal = ('options',)  # Allows for a better interface for ManyToMany fields

