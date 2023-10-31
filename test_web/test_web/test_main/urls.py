from django.urls import path
from .views import *
from . import views

urlpatterns = [

    path('', SubjectView.as_view(), name='subject_view'),
    path('tests/subject/<int:subject_id>/', TestView.as_view(), name='test_view'),
    path('questions/<int:test_id>', QuestionsView.as_view(), name='questions_list'),
    path('user_form/', user_form, name='user_form'),
    path('question/<int:pk>', QuestionView.as_view(), name='question_view')

]
# path('', views.index),
# path('test/', views.test_view),
# path('send_form/', views.submit_answer, name='submit_answer'),
# path('question_form/', question_form, name='question_view'),
