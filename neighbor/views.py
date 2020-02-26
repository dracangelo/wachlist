from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *






# Create your views here.

def home(request):
    if request.user.is_authenticated:
        if Join.objects.filter(user_id=request.user).exists():
            area = Areacode.objects.get(pk=request.user.join.area_id.id)
            posts = Post.objects.filter(post_area=request.user.join.area_id.id)
            businesses = Business.objects.filter(biz_area=request.user.join.area_id.id)
            return render(request, 'current_area.html', {"area": area, "businesses": businesses, "posts": posts})
        else:
            areas = Areacode.all_areacodes()
            return render(request, 'index.html', {"areas": areas})
    else:
        areas = Areacode.all_areacodes()
        return render(request, 'index.html', {"areas": areas})
    

@login_required
def add_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('home')

    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})


@login_required
def profile(request, username):
    profile = User.objects.get(username=username)
    try:
        profile_info = Profile.get_profile(profile.id)
    except:
        profile_info = Profile.filter_by_id(profile.id)
    businesses = Business.get_profile_businesses(profile.id)
    title = f'@{profile.username}'
    return render(request, 'profile.html', {'title': title, 'profile': profile, 'profile_info': profile_info, 'businesses': businesses})

@login_required
def add_area(request):
    current_user = request.user
    if request.method == 'POST':
        form = AddAreaForm(request.POST, request.FILES)
        if form.is_valid():
            area = form.save(commit=False)
            area.user_profile = current_user
            area.save()
        return redirect('homepage')

    else:
        form = AddAreaForm()
    return render(request, 'add_area.html', {"form": form})