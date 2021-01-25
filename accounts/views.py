from django.shortcuts import render, redirect

# Create your views here.
from .forms import SignUpForm, UserForm, ProfileForm
from .models import Profile
from django.contrib.auth import authenticate, login
from django.urls.base import reverse


def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('accounts/profile')

    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
    profile = Profile.objects.get(user=request.user)

    return render(request, 'profiles/profile.html', {'profile': profile})


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form_usr = UserForm(request.POST, instance=request.user)
        form_pro = ProfileForm(request.POST, request.FILES, instance=profile)

        if form_pro.is_valid and form_usr.is_valid:
            form_usr.save()
            form_pro_save = form_pro.save(commit=False)
            form_pro_save.user = request.user
            form_pro_save.save()

            return redirect(reverse('accounts:profile'))

    else:
        UserForm(instance=request.user)
        ProfileForm(instance=profile)

    return render(request, 'profiles/profile_edit.html', {'form_usr': UserForm(instance=request.user), 'form_pro': ProfileForm(instance=profile)})
