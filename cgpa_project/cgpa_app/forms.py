from django import forms
from .models import*

class student_add_form(forms.ModelForm):
    class Meta:
        model = Student_Model
        fields = ('__all__')

class subjects_add_form(forms.ModelForm):
    class Meta:
        model = Subjects_Model
        fields = ('__all__')
        
class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade_model
        fields = ['student', 'student_sub', 'marks']