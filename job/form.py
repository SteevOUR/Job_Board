from django import forms
from .models import Apply, Job


class ApplyForm(forms.ModelForm):

    class Meta:

        model = Apply
        fields = ['name', 'email', 'website', 'cv', 'cover_letter']


class JobForm(forms.ModelForm):

    class Meta:

        model = Job
        fields = ['title', 'description', 'job_type', 'vacancy',
                  'salary', 'experience', 'category', 'image']  # '__all__' # exclude = ('slug', 'owner')
