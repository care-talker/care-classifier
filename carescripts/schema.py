from typing import List, Optional
import strawberry
from strawberry_django import mutations
from .types import *


@strawberry.type
class Query:
    skill: Skill = strawberry.django.field()
    skills: List[Skill] = strawberry.django.field()
    userSkill: UserSkill = strawberry.django.field()
    userSkills: List[UserSkill] = strawberry.django.field()
    subject: Subject = strawberry.django.field()
    subjects: List[Subject] = strawberry.django.field()
    lesson: Lesson = strawberry.django.field()
    lessons: List[Lesson] = strawberry.django.field()
    expectation: Expectation = strawberry.django.field()
    expectations: List[Expectation] = strawberry.django.field()
    learningObjective: LearningObjective = strawberry.django.field()
    learningObjectives: List[LearningObjective] = strawberry.django.field()
    mode: Mode = strawberry.django.field()
    modes: List[Mode] = strawberry.django.field()
    question: Question = strawberry.django.field()
    questions: List[Question] = strawberry.django.field()
    assignment: Assignment = strawberry.django.field()
    assignments: List[Assignment] = strawberry.django.field()
    userAssignment: UserAssignment = strawberry.django.field()
    userAssignments: List[UserAssignment] = strawberry.django.field()
    session: Session = strawberry.django.field()
    sessions: List[Session] = strawberry.django.field()


@strawberry.type
class Mutation:
    createSkill: Skill = mutations.create(SkillPartialInput)
    createSkills: List[Skill] = mutations.create(SkillPartialInput)
    updateSkills: List[Skill] = mutations.update(SkillPartialInput)
    deleteSkills: List[Skill] = mutations.delete()
    createUserSkill: UserSkill = mutations.create(UserSkillPartialInput)
    createUserSkills: List[UserSkill] = mutations.create(UserSkillPartialInput)
    updateUserSkills: List[UserSkill] = mutations.update(UserSkillPartialInput)
    deleteUserSkills: List[UserSkill] = mutations.delete()
    createSubject: Subject = mutations.create(SubjectPartialInput)
    createSubjects: List[Subject] = mutations.create(SubjectPartialInput)
    updateSubjects: List[Subject] = mutations.update(SubjectPartialInput)
    deleteSubjects: List[Subject] = mutations.delete()
    createLesson: Lesson = mutations.create(LessonPartialInput)
    createLessons: List[Lesson] = mutations.create(LessonPartialInput)
    updateLessons: List[Lesson] = mutations.update(LessonPartialInput)
    deleteLessons: List[Lesson] = mutations.delete()
    createExpectation: Expectation = mutations.create(ExpectationPartialInput)
    createExpectations: List[Expectation] = mutations.create(ExpectationPartialInput)
    updateExpectations: List[Expectation] = mutations.update(ExpectationPartialInput)
    deleteExpectations: List[Expectation] = mutations.delete()
    createLearningObjective: LearningObjective = mutations.create(
        LearningObjectivePartialInput
    )
    createLearningObjectives: List[LearningObjective] = mutations.create(
        LearningObjectivePartialInput
    )
    updateLearningObjectives: List[LearningObjective] = mutations.update(
        LearningObjectivePartialInput
    )
    deleteLearningObjectives: List[LearningObjective] = mutations.delete()
    createMode: Mode = mutations.create(ModePartialInput)
    createModes: List[Mode] = mutations.create(ModePartialInput)
    updateModes: List[Mode] = mutations.update(ModePartialInput)
    deleteModes: List[Mode] = mutations.delete()
    createQuestion: Question = mutations.create(QuestionPartialInput)
    createQuestions: List[Question] = mutations.create(QuestionPartialInput)
    updateQuestions: List[Question] = mutations.update(QuestionPartialInput)
    deleteQuestions: List[Question] = mutations.delete()
    createAssignment: Assignment = mutations.create(AssignmentPartialInput)
    createAssignments: List[Assignment] = mutations.create(AssignmentPartialInput)
    updateAssignments: List[Assignment] = mutations.update(AssignmentPartialInput)
    deleteAssignments: List[Assignment] = mutations.delete()
    createUserAssignment: UserAssignment = mutations.create(UserAssignmentPartialInput)
    createUserAssignments: List[UserAssignment] = mutations.create(
        UserAssignmentPartialInput
    )
    updateUserAssignments: List[UserAssignment] = mutations.update(
        UserAssignmentPartialInput
    )
    deleteUserAssignments: List[UserAssignment] = mutations.delete()
    createSession: Session = mutations.create(SessionPartialInput)
    createSessions: List[Session] = mutations.create(SessionPartialInput)
    updateSessions: List[Session] = mutations.update(SessionPartialInput)
    deleteSessions: List[Session] = mutations.delete()


schema = strawberry.Schema(query=Query, mutation=Mutation)
