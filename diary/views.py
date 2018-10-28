from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

from diary.forms import DiaryCreateForm
from diary.models import Diary


class IndexView(generic.ListView):
    model = Diary


def add(request):
    form = DiaryCreateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')

    context = {
        'form': form
    }
    return render(request, 'diary/input.html', context)


def update(request, pk):
    diary = get_object_or_404(Diary, pk=pk)
    form = DiaryCreateForm(request.POST or None, instance=diary)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')

    context = {
        'form': form
    }
    return render(request, 'diary/input.html', context)
