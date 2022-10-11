from typing import List

import strawberry

import strawberry_django
import strawberry_django.auth as auth
from strawberry_django import mutations

from .types import (
    Subject,
    SubjectInput,
    SubjectPartialInput,
    Lesson,
    LessonInput,
    LessonPartialInput,
    User,
    UserInput,
)


@strawberry.type
class Query:
    lesson: Lesson = strawberry_django.field()
    lessons: List[Lesson] = strawberry_django.field()

    subject: Subject = strawberry_django.field()
    subjects: List[Subject] = strawberry_django.field()


@strawberry.type
class Mutation:
    createLesson: Lesson = mutations.create(LessonInput)
    createLessons: List[Lesson] = mutations.create(LessonInput)
    updateLessons: List[Lesson] = mutations.update(LessonPartialInput)
    deleteLessons: List[Lesson] = mutations.delete()

    createSubject: Subject = mutations.create(SubjectInput)
    createSubjects: List[Subject] = mutations.create(SubjectInput)
    updateSubjects: List[Subject] = mutations.update(SubjectPartialInput)
    deleteSubjects: List[Subject] = mutations.delete()

    register: User = auth.register(UserInput)


schema = strawberry.Schema(query=Query, mutation=Mutation)
