from django.urls import reverse_lazy
from django.views import generic

from diary.forms import DiaryCreateForm
from diary.models import Diary


class IndexView(generic.ListView):
    model = Diary
    queryset = Diary.objects.all().order_by('-created_at')


class AddView(generic.CreateView):
    model = Diary
    form_class = DiaryCreateForm
    success_url = reverse_lazy('diary:index')


class UpdateView(generic.UpdateView):
    model = Diary
    form_class = DiaryCreateForm
    success_url = reverse_lazy('diary:index')


class DeleteView(generic.DeleteView):
    model = Diary
    success_url = reverse_lazy('diary:index')
