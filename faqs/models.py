from django.db import models


class FAQCategory(models.Model):

    class Meta:
        verbose_name_plural = 'FAQ Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class FAQ_QA(models.Model):

    class Meta:
        verbose_name_plural = 'FAQs'

    faq_category = models.ForeignKey(
        FAQCategory,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
