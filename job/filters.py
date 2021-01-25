import django_filters
from .models import Job


class JobFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    experience = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:

        model = Job
        fields = ['title', 'description', 'job_type', 'category', 'experience']
        # exclude = ['owner', 'published_at',
        # 'last_update_at', 'salary', 'vacancy', 'image', 'slug']
