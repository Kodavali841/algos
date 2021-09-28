from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Subject, Assignments
from .forms import SubjectForm


# Create your views here.
def index(request):
    subjects = Subject.objects.all()
    form = SubjectForm()
    context = {'subjects': subjects, 'form': form, }
    return render(request, 'index.html', context)
    
def create(request):
    form = SubjectForm(request.POST)
    form.save(commit=True)
    return HttpResponseRedirect(reverse('school:index'))


def assign(request):
    name = request.GET['name']
    # post = Post.objects.get(slug=slug)
    assignments = Assignments.objects.filter(subject=name)
    context = {'assigns': assignments, 'name':name }
    return render(request, 'assign.html', context)
