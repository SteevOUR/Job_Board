from django.shortcuts import render, redirect

# Create your views here.
from .models import Job, Category
from django.core.paginator import Paginator
from .form import ApplyForm, JobForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JobFilter
from accounts.models import City


def job_list(request):
    job_list = Job.objects.all()

    # Filter
    job_filter = JobFilter(request.GET, queryset=job_list)
    job_list = job_filter.qs
    # Pagination
    paginator = Paginator(job_list, 5)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    # For Template Name {URL}
    context = {'jobs': page_obj, 'all_jobs': job_list,
               'job_filter': job_filter}

    return render(request, 'job/job_list.html', context)


@login_required
def job_detail(request, slug, id):
    job_detail = Job.objects.get(slug=slug, id=id)

    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)

        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.job = job_detail
            form_save.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = ApplyForm()

    context = {'job': job_detail, 'form': form}  # For Template Name {URL}

    return render(request, 'job/job_detail.html', context)


@login_required
def add_job(request):

    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid:
            form_add = form.save(commit=False)
            form_add.owner = request.user
            form_add.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = JobForm()

    return render(request, 'job/add_job.html', {'form': form})


def home_page(request):
    job_list = Job.objects.all()
    category = Category.objects.all()
    cities_list = City.objects.all()
    context = {'all_jobs': job_list,
               'all_categories': category, 'all_cities': cities_list}

    return render(request, 'job/home_page.html', context)
