from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', home_page, name='home_page'),
    path('', CourseListView.as_view(), name='list'),
    path('create/', CourseCreateView.as_view(), name='create'),
    path('<int:pk>/', CourseDetailView.as_view(), name='details'),
    path('<int:pk>/update/', CourseUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CourseDeleteView.as_view(), name='delete')
]