from django.shortcuts import render, redirect
from django.utils import timezone, timesince
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import SettingsAuthForm, UpdateUsernameForm, UpdateProfileForm


def settings(request):
    if request.user.is_authenticated:
        return redirect('settings_account')
    else:
        return redirect('settings_account_personalization')


@login_required
def settings_account(request):

    form = SettingsAuthForm(request.POST or None)

    if form.is_valid():
        password = form.cleaned_data.get('password')
        username = request.user.username
        if authenticate(request, username = username, password = password):
            return redirect('home')
        else:
            form.add_error(field = None, error = 'The password you entered was incorrect.')

    context = {'form': form}
    return render(request, 'settings_yourChirperData_auth.html', context)


def settings_account_personalization(request):
    return render(request, 'settings_account_personalization.html')


@login_required
def settings_password(request):
    return render(request, 'settings_password.html')


@login_required
def settings_screenName(request):
    return render(request, 'settings_screenName.html')


@login_required
def settings_securityAndAccountAccess(request):
    return render(request, 'settings_securityAndAccountAccess.html')


@login_required
def settings_privacyAndSafety(request):
    return render(request, 'settings_privacyAndSafety.html')


@login_required
def settings_notifications(request):
    return render(request, 'settings_notifications.html')


@login_required
def settings_accessibilityDisplayAndLanguages(request):
    return render(request, 'settings_accessibilityDisplayAndLanguages.html')


def settings_about(request):
    return render(request, 'settings_about.html')


def settings_yourChirperData(request):
    return render(request, 'settings_yourChirperData.html')


def settings_yourChirperData_account(request):
    return render(request, 'settings_yourChirperData_account.html')


@login_required
def settings_phone(request):
    return render(request, 'settings_phone.html')


@login_required
def settings_addPhone_auth(request):
    return render(request, 'settings_addPhone_auth.html')


@login_required
def settings_addPhone(request):
    return render(request, 'settings_addPhone.html')


@login_required
def settings_deletePhone(request):
    return render(request, 'settings_deletePhone.html')



@login_required
def settings_email(request):
    return render(request, 'settings_email.html')


@login_required
def settings_addEmail_auth(request):
    return render(request, 'settings_addEmail_auth.html')


@login_required
def settings_addEmail(request):
    return render(request, 'settings_addEmail.html')


@login_required
def settings_audienceAndTagging(request):
    return render(request, 'settings_audienceAndTagging.html')


@login_required
def settings_country(request):
    return render(request, 'settings_country.html')


def settings_languages(request):
    return render(request, 'settings_languages.html')


def settings_yourChirperData_gender(request):
    return render(request, 'settings_yourChirperData_gender.html')


def settings_yourChirperData_age(request):
    return render(request, 'settings_yourChirperData_age.html')


@login_required
def settings_trends(request):
    return render(request, 'settings_trends.html')


@login_required
def settings_contentPreferences(request):
    return render(request, 'settings_contentPreferences.html')


@login_required
def settings_appsAndSessions(request):
    return render(request, 'settings_appsAndSessions.html')


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