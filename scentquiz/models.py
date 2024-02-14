from django.db import models

class ScentOption(models.Model):
    text = models.CharField(max_length=100)
    scent_profile = models.CharField(max_length=50)  # Field to store the scent profile

    def __str__(self):
        return self.text

class Question(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class QuizQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    options = models.ManyToManyField(ScentOption)

    def __str__(self):
        return self.question.text

