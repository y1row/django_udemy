from django import forms

from diary.models import Diary


class DiaryCreateForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = '__all__'
