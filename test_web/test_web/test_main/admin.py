from django.contrib import admin
from .models import *


class TestAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}


class SubjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}


class QuestionAdmin(admin.ModelAdmin):
    exclude = ('user_answer',)
    list_display = (
        'test_title',
        'question_title',
        'question_text',
        'answer1', 'answer2', 'answer3', 'answer4',
        'is_correct'
                    )


admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(User)
