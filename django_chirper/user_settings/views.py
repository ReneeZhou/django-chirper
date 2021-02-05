from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UpdateUsernameForm, UpdateProfileForm



@login_required
def settings_profile(request):
    if request.method == 'POST':
        u_form = UpdateUsernameForm(request.POST, instance = request.user) 
        p_form = UpdateProfileForm(request.POST, request.FILES, instance = request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('home')
        

    elif request.method == 'GET':
        u_form = UpdateUsernameForm(instance = request.user)
        p_form = UpdateProfileForm(instance = request.user.profile)


    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'settings_profile.html', context)