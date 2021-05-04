from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect

from core.forms import EditProfile, ProfileForm, ItemForm
from core.models import File, Profile


def register(request):
    form=UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'user has been registered')
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


@login_required(login_url='login')
def profile(request):
    profile = Profile.objects.filter(user=request.user).first()

    if request.method == 'POST':
        form = EditProfile(request.POST, instance=request.user)
        profle_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid() and profle_form.is_valid():
            user_form = form.save()
            custom_form = profle_form.save(False)
            custom_form.user = user_form
            custom_form.save()
            messages.success(request, 'user profile has been updated')
            return redirect('/')
        else:
            messages.error(request, 'Submission Error')
    if request.method == 'GET':
        form = EditProfile(instance=request.user)
        profle_form = ProfileForm(instance=profile)
        context = {
            'form': form,
            'profile_form': profle_form
        }
        return render(request, 'profile.html', context)


def home(request):
    file = File.objects.all()
    context = {
        'files': file
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')
def watch(request, id):
    file = File.objects.get(id=id)
    context = {
        'file': file
    }
    return render(request, 'watch.html', context)

@login_required(login_url='login')
def add_file(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'File added successfully')
            return redirect('/')
        else:
            messages.error(request, 'File submission error')
            return redirect('add_file')
    context = {
        'items': form
    }
    return render(request, 'add_file.html', context)

@login_required(login_url='login')
def update_file(request, id):
    file = File.objects.get(id=id)
    form = ItemForm(instance=file)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=file)
        if form.is_valid():
            form.save()
            messages.success(request, 'file update successfully')
            return redirect('/')
        else:
            messages.error(request, 'File submission error')
    context = {
        'file': file,
        'items': form
    }
    return render(request, 'update_file.html', context)

@login_required(login_url='login')
def delete(request, id):
    order = File.objects.get(id=id)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'file': order}
    return render(request, 'delete_file.html', context)

@login_required(login_url='login')
def handler(request, action):
    file = File.objects.filter(category=action)
    context = {
        'files': file
    }
    return render(request, 'handler.html', context)

@login_required(login_url='login')
def me(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'me.html', context)
