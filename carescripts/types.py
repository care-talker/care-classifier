from typing import List
from django.contrib.auth import get_user_model
from strawberry import auto
import strawberry_django
from . import models


@strawberry_django.type(get_user_model())
class User:
    id: auto
    username: auto
    password: auto
    email: auto


@strawberry_django.input(get_user_model())
class UserInput:
    username: auto
    password: auto
    email: auto


# filters
@strawberry_django.filters.filter(models.Skill, lookups=True)
class SkillFilter:
    id: auto
    name: auto


@strawberry_django.filters.filter(models.UserSkill, lookups=True)
class UserSkillFilter:
    id: auto
    level: auto


@strawberry_django.filters.filter(models.Subject, lookups=True)
class SubjectFilter:
    id: auto
    name: auto


@strawberry_django.filters.filter(models.Lesson, lookups=True)
class LessonFilter:
    id: auto
    name: auto


@strawberry_django.filters.filter(models.Expectation, lookups=True)
class ExpectationFilter:
    id: auto
    level: auto


@strawberry_django.filters.filter(models.LearningObjective, lookups=True)
class LearningObjectiveFilter:
    id: auto
    level: auto


@strawberry_django.filters.filter(models.Mode, lookups=True)
class ModeFilter:
    id: auto
    name: auto


@strawberry_django.filters.filter(models.Question, lookups=True)
class QuestionFilter:
    id: auto
    text: auto
    lesson: LessonFilter
    answer: auto
    title: auto


@strawberry_django.filters.filter(models.Assignment, lookups=True)
class AssignmentFilter:
    id: auto
    releaseDate: auto
    dueDate: auto
    closeDate: auto


@strawberry_django.filters.filter(models.UserAssignment, lookups=True)
class UserAssignmentFilter:
    id: auto
    complete: auto


@strawberry_django.filters.filter(models.Session, lookups=True)
class SessionFilter:
    id: auto
    startDate: auto
    endDate: auto


# orders
@strawberry_django.ordering.order(models.Skill)
class SkillOrder:
    name: auto
    userskills: "UserSkillOrder"
    learningobjectives: "LearningObjectiveOrder"


@strawberry_django.ordering.order(models.UserSkill)
class UserSkillOrder:
    level: auto
    skill: SkillOrder
    expectations: "ExpectationOrder"


@strawberry_django.ordering.order(models.Subject)
class SubjectOrder:
    name: auto
    lessons: "LessonOrder"


@strawberry_django.ordering.order(models.Lesson)
class LessonOrder:
    name: auto
    subject: SubjectOrder
    questions: "QuestionOrder"
    assignments: "AssignmentOrder"


@strawberry_django.ordering.order(models.Expectation)
class ExpectationOrder:
    skill: UserSkillOrder
    level: auto
    questions: "QuestionOrder"


@strawberry_django.ordering.order(models.LearningObjective)
class LearningObjectiveOrder:
    skill: SkillOrder
    level: auto
    questions: "QuestionOrder"


@strawberry_django.ordering.order(models.Mode)
class ModeOrder:
    name: auto
    questions: "QuestionOrder"


@strawberry_django.ordering.order(models.Question)
class QuestionOrder:
    text: auto
    mode: ModeOrder
    lesson: LessonOrder
    answer: auto
    title: auto

    expectation: ExpectationOrder
    objective: LearningObjectiveOrder


@strawberry_django.ordering.order(models.Assignment)
class AssignmentOrder:
    releaseDate: auto
    dueDate: auto
    closeDate: auto
    lesson: LessonOrder
    userassignments: "UserAssignmentOrder"


@strawberry_django.ordering.order(models.UserAssignment)
class UserAssignmentOrder:
    complete: auto
    assignment: AssignmentOrder
    sessions: "SessionOrder"


@strawberry_django.ordering.order(models.Session)
class SessionOrder:
    userAssignment: UserAssignmentOrder
    startDate: auto
    endDate: auto


# types
@strawberry_django.type(
    models.Skill, filters=SkillFilter, order=SkillOrder, pagination=True
)
class Skill:
    id: auto
    name: auto
    userskills: "UserSkill"
    learningobjectives: "LearningObjective"


@strawberry_django.type(
    models.UserSkill, filters=UserSkillFilter, order=UserSkillOrder, pagination=True
)
class UserSkill:
    id: auto
    level: auto
    skill: Skill


@strawberry_django.type(
    models.Subject, filters=SubjectFilter, order=SubjectOrder, pagination=True
)
class Subject:
    id: auto
    name: auto
    lessons: "Lesson"


@strawberry_django.type(
    models.Question, filters=QuestionFilter, order=QuestionOrder, pagination=True
)
class Question:
    id: auto
    text: auto
    mode: "Mode"
    lesson: "Lesson"
    answer: auto
    title: auto

    expectation: "Expectation"
    objective: "LearningObjective"


@strawberry_django.type(
    models.Lesson, filters=LessonFilter, order=LessonOrder, pagination=True
)
class Lesson:
    id: auto
    name: auto
    subject: "Subject"
    questions: List[Question]
    assignments: "Assignment"


@strawberry_django.type(
    models.Expectation,
    filters=ExpectationFilter,
    order=ExpectationOrder,
    pagination=True,
)
class Expectation:
    id: auto
    skill: Skill
    level: auto
    questions: "Question"


@strawberry_django.type(
    models.LearningObjective,
    filters=LearningObjectiveFilter,
    order=LearningObjectiveOrder,
    pagination=True,
)
class LearningObjective:
    id: auto
    skill: Skill
    level: auto
    questions: "Question"


@strawberry_django.type(
    models.Mode, filters=ModeFilter, order=ModeOrder, pagination=True
)
class Mode:
    id: auto
    name: auto
    questions: "Question"


@strawberry_django.type(
    models.Assignment, filters=AssignmentFilter, order=AssignmentOrder, pagination=True
)
class Assignment:
    id: auto
    releaseDate: auto
    dueDate: auto
    closeDate: auto
    lesson: Lesson
    userassignments: "UserAssignment"


@strawberry_django.type(
    models.UserAssignment,
    filters=UserAssignmentFilter,
    order=UserAssignmentOrder,
    pagination=True,
)
class UserAssignment:
    id: auto
    complete: auto
    assignment: Assignment
    sessions: "Session"


@strawberry_django.type(
    models.Session, filters=SessionFilter, order=SessionOrder, pagination=True
)
class Session:
    id: auto
    userAssignment: UserAssignment
    startDate: auto
    endDate: auto


# input types
@strawberry_django.input(models.Skill)
class SkillInput:
    id: auto
    name: auto
    userskills: auto
    learningobjectives: auto


@strawberry_django.input(models.UserSkill)
class UserSkillInput:
    id: auto
    level: auto
    skill: auto


@strawberry_django.input(models.Subject)
class SubjectInput:
    id: auto
    name: auto
    lessons: auto


@strawberry_django.input(models.Lesson)
class LessonInput:
    id: auto
    name: auto
    subject: auto
    questions: auto
    assignments: auto


@strawberry_django.input(models.Expectation)
class ExpectationInput:
    id: auto
    skill: auto
    level: auto
    questions: auto


@strawberry_django.input(models.LearningObjective)
class LearningObjectiveInput:
    id: auto
    skill: auto
    level: auto
    questions: auto


@strawberry_django.input(models.Mode)
class ModeInput:
    id: auto
    name: auto
    questions: auto


@strawberry_django.input(models.Question)
class QuestionInput:
    id: auto
    text: auto
    mode: auto
    lesson: auto
    answer: auto
    title: auto

    expectation: auto
    objective: auto


@strawberry_django.input(models.Assignment)
class AssignmentInput:
    id: auto
    releaseDate: auto
    dueDate: auto
    closeDate: auto
    lesson: auto
    userassignments: auto


@strawberry_django.input(models.UserAssignment)
class UserAssignmentInput:
    id: auto
    complete: auto
    assignment: auto
    sessions: auto


@strawberry_django.input(models.Session)
class SessionInput:
    id: auto
    userAssignment: auto
    startDate: auto
    endDate: auto


# partial inputs
@strawberry_django.input(models.Skill, partial=True)
class SkillPartialInput(SkillInput):
    pass


@strawberry_django.input(models.UserSkill, partial=True)
class UserSkillPartialInput(UserSkillInput):
    pass


@strawberry_django.input(models.Subject, partial=True)
class SubjectPartialInput(SubjectInput):
    pass


@strawberry_django.input(models.Lesson, partial=True)
class LessonPartialInput(LessonInput):
    pass


@strawberry_django.input(models.Expectation, partial=True)
class ExpectationPartialInput(ExpectationInput):
    pass


@strawberry_django.input(models.LearningObjective, partial=True)
class LearningObjectivePartialInput(LearningObjectiveInput):
    pass


@strawberry_django.input(models.Mode, partial=True)
class ModePartialInput(ModeInput):
    pass


@strawberry_django.input(models.Question, partial=True)
class QuestionPartialInput(QuestionInput):
    pass


@strawberry_django.input(models.Assignment, partial=True)
class AssignmentPartialInput(AssignmentInput):
    pass


@strawberry_django.input(models.UserAssignment, partial=True)
class UserAssignmentPartialInput(UserAssignmentInput):
    pass


@strawberry_django.input(models.Session, partial=True)
class SessionPartialInput(SessionInput):
    pass
