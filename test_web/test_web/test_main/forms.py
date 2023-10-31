from django import forms
from .models import *


class UserForm(forms.ModelForm):
    user_email = forms.EmailField(label='Электронная почта',
                                  widget=forms.EmailInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    oblast = forms.CharField(label='Область',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'autocomplete': 'off'}))
    city = forms.CharField(label='Город',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'autocomplete': 'off'}))
    gender = forms.ChoiceField(label='Пол', widget=forms.RadioSelect, choices=User.GENDER_CHOICE)
    age = forms.CharField(label='Возраст',
                          widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'min': 6, 'max': 120, 'autocomplete': 'off'}))
    organization = forms.CharField(label='Организация',
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'autocomplete': 'off'}))

    class Meta:
        model = User
        fields = ['user_email', 'oblast', 'city', 'gender', 'age', 'organization']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['user_answer']

# class QuestionForm(forms.Form):
#     # class Meta:
#     #     model = Question
#     #     fields = ['__all__']
#
#     user_answer = forms.ChoiceField(choices=Question.ANSWERS_CHOICE, widget=forms.RadioSelect)
#