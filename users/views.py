from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ManagerRegisterForm, UserPasswordChangeForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import Activity

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.profile.IDnum = form.cleaned_data.get('IDnum')
			user.profile.Role = form.cleaned_data.get('classification')
			user.profile.SecurityQuestion = form.cleaned_data.get('SecurityQ')
			user.profile.SecurityAnswer = form.cleaned_data.get('SecuirtyA')
			user.save()
			username = form.cleaned_data.get('username')

			message = 'Registered profile'
			updateActivity(user.profile, 'Addition', message)

			messages.success(request, f'Your account has been created! You may log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})
"""
@login_required
def change_password(request):
    if request.method == 'POST':
        form = UserPasswordChangeForm(request.user, request.POST)

        if form.is_valid():
        	if  form.cleaned_data.get('SecuirtyA') == request.user.profile.SecurityAnswer:
	            user = form.save()
	            update_session_auth_hash(request, user)  # Important!
	            messages.success(request, 'Your password was successfully updated!')
	            return redirect('change_password')
	        else:
	            messages.error(request, 'Please correct answer to ' + request.user.profile.SecurityQuestion)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserPasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })	
"""
@login_required
def change_password(request):
    if request.method == 'POST':
        form = UserPasswordChangeForm(request.user, request.POST)

        if form.is_valid():
	            user = form.save()
	            update_session_auth_hash(request, user)  # Important!
	            messages.success(request, 'Your password was successfully updated!')
	            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserPasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })	


@login_required
def profile(request):
	if request.method == 'POST':
		#u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		#if u_form.is_valid() and p_form.is_valid():
		if p_form.is_valid():
			#u_form.save()
			p_form.save()

			message = 'Updated their profile'
			updateActivity(request.user.profile, 'Changed', message)

			messages.success(request, f'Your account has been Updated!')
			return redirect('profile')
	else:
		#u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)


	context = {
		#'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'users/profile.html', context)

def manager(request):
	if request.method == 'POST':
		form = ManagerRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.profile.IDnum = form.cleaned_data.get('IDnum')
			user.profile.Role = form.cleaned_data.get('classification')
			user.profile.SecurityQuestion = form.cleaned_data.get('SecurityQ')
			user.profile.SecurityAnswer = form.cleaned_data.get('SecuirtyA')
			user.save()
			username = form.cleaned_data.get('username')

			message = 'created new manager "' + username + '"'
			updateActivity(request.user.profile, 'Addition', message)

			messages.success(request, f'Your account has been created! You may log in')
			return redirect('new_manager')
	else:
		form = ManagerRegisterForm()
	return render(request, 'users/create_manager.html', {'form': form})

def updateActivity(user, action, content):
	newactivity = Activity(
		user = user,
		action = action,
		content = content,
	)
	newactivity.save()