from typing import List

from django.contrib.auth import get_user_model
from strawberry import auto

import strawberry_django

from . import models


# filters


@strawberry_django.filters.filter(models.Lesson, lookups=True)
class LessonFilter:
    id: auto
    name: auto
    subject: "SubjectFilter"


@strawberry_django.filters.filter(models.Subject, lookups=True)
class SubjectFilter:
    id: auto
    name: auto
    lessons: LessonFilter


# order


@strawberry_django.ordering.order(models.Lesson)
class LessonOrder:
    name: auto
    subject: "SubjectOrder"


@strawberry_django.ordering.order(models.Subject)
class SubjectOrder:
    name: auto
    lesson: LessonOrder


# types


@strawberry_django.type(
    models.Lesson, filters=LessonFilter, order=LessonOrder, pagination=True
)
class Lesson:
    id: auto
    name: auto
    subject: "Subject"


@strawberry_django.type(
    models.Subject, filters=SubjectFilter, order=SubjectOrder, pagination=True
)
class Subject:
    id: auto
    name: auto
    lessons: List[Lesson]


@strawberry_django.type(get_user_model())
class User:
    id: auto
    username: auto
    password: auto
    email: auto


# input types


@strawberry_django.input(models.Lesson)
class LessonInput:
    id: auto
    name: auto
    subject: auto


@strawberry_django.input(models.Subject)
class SubjectInput:
    id: auto
    name: auto
    lessons: auto


@strawberry_django.input(get_user_model())
class UserInput:
    username: auto
    password: auto
    email: auto


# partial input types


@strawberry_django.input(models.Lesson, partial=True)
class LessonPartialInput(LessonInput):
    pass


@strawberry_django.input(models.Subject, partial=True)
class SubjectPartialInput(SubjectInput):
    pass
