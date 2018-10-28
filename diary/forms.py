from django import forms

from diary.models import Diary


class DiaryCreateForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # class
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        # placeholder
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルを入力してください'
        self.fields['text'].widget.attrs['placeholder'] = '本文を入力してください'
