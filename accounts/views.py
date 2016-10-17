from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from .forms import LoginForm, Register, Register2, Edit
from .models import RealUsers
from django.contrib.auth.models import User
from django.forms import inlineformset_factory

# Create your views here.


def index(request):
    template = 'index.html'
    if request.user.is_authenticated():
        return redirect('/eCaretaker')
    return render(request, template)


def loguserin(request):
    form = LoginForm(data=request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")#request.POST.get('username', False)
        password = form.cleaned_data.get("password")#request.POST.get('password', False)
        user = authenticate(username=username, password = password)
        if user is not None:
            login(request, user)
            # return HttpResponseRedirect("eCaretaker:index")
            return redirect('/eCaretaker')
    context = {
        'form': form
    }
    return render(request, 'account/login.html', context)


def register(request, authentication_form=(Register, Register2)):
    form = authentication_form[0](request.POST or None)
    form2 = authentication_form[1](request.POST or None)

    if form.is_valid() and form2.is_valid:
        instance = form.save(commit=False)
        instance2 = form2.save(commit=False)
        instance.save()
        instance2.user = instance
        instance2.save()
        #   Display success message
        messages.success(request, "Successfully registered")
        print("user is registered")
        return HttpResponseRedirect('/login/')

    context = {
        'form': form,
        'form2': form2,
    }
    return render(request, 'account/register.html', context)


def logoff(request):
    logout(request)
    messages.success(request, "You have successfully log out")
    return HttpResponseRedirect('/login/')


def profile(request):
    user = User.objects.get(username=request.user.username)
    # form = inlineformset_factory(User, RealUsers, exclude=['updated'])
    if request.method == "POST":
        formset_user = Edit(request.POST, instance=user)
        formset_real = Register2(request.POST, instance=user.realusers)
        if formset_user.is_valid() and formset_real.is_valid():
            formset_user.save(commit=False)
            formset_real.save(commit=False)
            formset_user.save()
            formset_real.save()
            messages.success(request, "Your profile has been updated successfully")
            return HttpResponseRedirect("/eCaretaker/")
    else:
        formset_user = Edit(instance=user)
        formset_real = Register2(instance=user.realusers)

    context = {
        'formset_user': formset_user,
        'formset_real': formset_real,
        'username': user.username,
        'full_name': user.realusers.get_full_name()
    }
    return render(request, 'account/profile.html', context)