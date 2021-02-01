from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm, HUserLoginForm


# def home_notauth(request):
#     if request.user.is_authenticated:
#         return redirect('home')
    
#     form = HUserLoginForm()
#     if request.method == 'GET':
#         return render(request, 'home_notauth.html', {'form': form})
#     elif request.method == 'POST':
#         if form.is_valid():
#             return redirect('home')
#         else: 
#             messages.warning(request, 
#                             'There was unusual login activity on your account. \
#                                 To help keep your account safe, \
#                                     please enter your phone number or email address to verify it’s you.')
#             return redirect('login')


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'signup.html', {'form': form})