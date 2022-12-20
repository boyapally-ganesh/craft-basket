from . forms import userregister
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, PasswordChangeForm, SetPasswordForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import usereditform
def userregisterview(request):
   if request.method=="POST":
      userform = userregister(request.POST)
      if userform.is_valid():
        userform.save()
        messages.success(request, 'account as createdsuceesfully😎')
        userform =userregister()
   else:
        userform =userregister()
   return render(request, 'users/signup.html',{'form':userform})

def login_form(request):
    if not request.user.is_authenticated:
      if request.method == 'POST':
         lg = AuthenticationForm(request=request, data=request.POST)
         if lg.is_valid():
            uname=lg.cleaned_data['username']
            upass=lg.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
               login(request, user)
               return HttpResponseRedirect('/')
      else:
        lg = AuthenticationForm()
      return render(request, 'users/login.html',{'form':lg})
    else:
        return HttpResponseRedirect('/profile/')

def user_logout(request):  
    logout(request)

    return HttpResponseRedirect('/')


#profile edit 
"""def user_profile(request):
   if request.user.is_authenticated:
        fm = UserChangeForm(instance=request.user)
        return render(request, 'users/useredit.html',{'form':fm})
   else:
      return HttpResponseRedirect('')"""
def user_profile(request):
    if request.method == 'POST':
        user_form = usereditform(request.POST, instance=request.user)
        passreset = SetPasswordForm(user=request.user, data=request.POST)
        #profile_form = ProfileForm(request.POST, instance=request.user.profile)
        #if user_form.is_valid() and profile_form.is_valid():
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect('/')
        if passreset.is_valid():
            passreset.save()
            #profile_form.save()
            return HttpResponseRedirect('/')
        else:
            #print(user_form.errors, profile_form.errors)
            print(user_form.errors)

    elif request.method == "GET":
        user_form = usereditform(instance=request.user)
        passreset = SetPasswordForm(user=request.user)
        #profile_form = ProfileForm(instance=request.user.profile)
        #return render(request, 'user_data.html', {'user_form': user_form, 'profile_form': profile_form})
        return render(request, 'users/edit.html', {'update': user_form,'password':passreset})

"""
def change_passwordwithout(request): 
    if  request.user.is_authenticated:
     if request.method=='POST':
        ps = SetPasswordForm(user=request.user, data=request.POST)
        if ps.is_valid():
           ps.save()
           #this is used to redirect profile after password change otherwise it shows logoutpage
           update_session_auth_hash(request, ps.user)
           #this is show to the user password changesuccesfully
           messages.success(request, 'password changed succefully!!😍')
           return HttpResponseRedirect('') 
     else:
        ps = SetPasswordForm(user=request.user)

     return render(request, 'users/edit.html', {'password':ps})
    else:
        return HttpResponseRedirect('/login/')"""
"""
def change_passwordwithout(request):
    if request.method == 'POST':
        passreset = SetPasswordForm(user=request.POST, data=request.POST)
        #profile_form = ProfileForm(request.POST, instance=request.user.profile)
        #if user_form.is_valid() and profile_form.is_valid():
        if passreset.is_valid():
            passreset.save()
            #profile_form.save()
            return HttpResponseRedirect('/')
        else:
            #print(user_form.errors, profile_form.errors)
            print(user_form.errors)

    elif request.method == "GET":
        passreset = SetPasswordForm(user=request.user)
        #profile_form = ProfileForm(instance=request.user.profile)
        #return render(request, 'user_data.html', {'user_form': user_form, 'profile_form': profile_form})
        return render(request, 'users/edit.html', {'password': user_form})
"""
def category(request):
    return render(request, 'post/categories.html')