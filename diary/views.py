from django.shortcuts import render, redirect

from diary.forms import DiaryCreateForm
from diary.models import Diary


def index(request):
    context = {
        'diary_list': Diary.objects.all().order_by('-created_at'),
    }
    return render(request, 'diary/index.html', context)


def add(request):
    form = DiaryCreateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')

    context = {
        'form': DiaryCreateForm()
    }
    return render(request, 'diary/input.html', context)
