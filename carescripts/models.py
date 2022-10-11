from django.db import models


class Lesson(models.Model):
    name = models.CharField(max_length=20)
    subject = models.ForeignKey(
        "Subject",
        blank=True,
        null=True,
        related_name="lessons",
        on_delete=models.CASCADE,
    )


class Subject(models.Model):
    name = models.CharField(max_length=20)
