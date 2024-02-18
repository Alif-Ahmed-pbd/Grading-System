from django.contrib import admin
from django.urls import path
from cgpa_app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('add_student/', add_student, name='add_student'),
    path('add_subjects/', add_subjects, name='add_subjects'),
    path('student_list/', student_list, name='student_list'),
    path('subject_list/', subject_list, name='subject_list'),
    path('add_subjects_to_student/<int:student_id>/', add_subjects_to_student, name='add_subjects_to_student'),
    path('user_delete/<str:id>/', user_delete, name='user_delete')

]
