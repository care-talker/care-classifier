from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=20)


class UserSkill(models.Model):
    level = models.IntegerField()
    skill = models.ForeignKey(
        "Skill",
        blank=True,
        null=True,
        related_name="userskills",
        on_delete=models.CASCADE,
    )


class Subject(models.Model):
    name = models.CharField(max_length=20)


class Lesson(models.Model):
    name = models.CharField(max_length=20)
    subject = models.ForeignKey(
        "Subject",
        blank=True,
        null=True,
        related_name="lessons",
        on_delete=models.CASCADE,
    )


class Expectation(models.Model):
    skill = models.ForeignKey(
        "UserSkill",
        blank=True,
        null=True,
        related_name="expectations",
        on_delete=models.CASCADE,
    )
    level = models.IntegerField()


class LearningObjective(models.Model):
    skill = models.ForeignKey(
        "Skill",
        blank=True,
        null=True,
        related_name="learningobjectives",
        on_delete=models.CASCADE,
    )
    level = models.IntegerField()


class Mode(models.Model):
    name = models.CharField(max_length=20)


class Question(models.Model):
    text = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    mode = models.ForeignKey(
        "Mode",
        blank=True,
        null=True,
        related_name="questions",
        on_delete=models.CASCADE,
    )
    lesson = models.ForeignKey(
        "Lesson",
        blank=True,
        null=True,
        related_name="questions",
        on_delete=models.CASCADE,
    )
    answer = models.CharField(max_length=250)
    expectation = models.ForeignKey(
        "Expectation",
        blank=True,
        null=True,
        related_name="questions",
        on_delete=models.CASCADE,
    )
    objective = models.ForeignKey(
        "LearningObjective",
        blank=True,
        null=True,
        related_name="questions",
        on_delete=models.CASCADE,
    )


class Assignment(models.Model):
    releaseDate = models.DateField()
    dueDate = models.DateField()
    closeDate = models.DateField()
    lesson = models.ForeignKey(
        "Lesson",
        blank=True,
        null=True,
        related_name="assignments",
        on_delete=models.CASCADE,
    )


class UserAssignment(models.Model):
    complete = models.BooleanField()
    assignment = models.ForeignKey(
        "Assignment",
        blank=True,
        null=True,
        related_name="userassignments",
        on_delete=models.CASCADE,
    )


class Session(models.Model):
    userAssignment = models.ForeignKey(
        "UserAssignment",
        blank=True,
        null=True,
        related_name="sessions",
        on_delete=models.CASCADE,
    )
    startDate = models.DateField()
    endDate = models.DateField()
