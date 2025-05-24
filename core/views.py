from django.shortcuts import HttpResponse, render
from django.views import View
from django.urls import reverse_lazy
from .models import Course
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import CourseForm

def home_page(request):
    courses = Course.objects.all()
    context = {
        'courses':courses,
        # 'student':student,
        # 'department':department,
        # 'employees':employees,
    }
    return render(request, 'dashboard.html' , context)

class CourseListView(ListView):
    model = Course
    queryset = Course.objects.all()
    template_name = 'course_list.html'
    context_object_name = 'courses'

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course_form.html'
    success_url = reverse_lazy('list')
    
class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'
    context_object_name = 'course'

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'course_form.html'
    success_url = reverse_lazy('list')


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('list')

# class HomeView(View):
#     def get(self, request):
#         return HttpResponse("Home Page CBVs")

