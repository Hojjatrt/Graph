from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db import transaction
from .models import *
from .forms import UserForm, ProfileForm
from django.utils.translation import ugettext_lazy as _


@login_required
@transaction.atomic
def update_profile(request):
    context = {}
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user = User.objects.get(username=request.user.username)
        if user.is_authenticated and user.profile.stu_num == '':
            context['stu_num'] = _('You must to fill your student number field')

        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        context['user_form'] = user_form
        context['profile_form'] = profile_form
    return render(request, 'accounts/profile.html', context)


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def Login(request):
    print("login")
    context = {'user': request.user}
    return render(request, 'accounts/registrations/login.html', context)
