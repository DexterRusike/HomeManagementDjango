from django.shortcuts import render, redirect, get_object_or_404
from chore.forms import UserForm, UserProfileInfoForm, UserProfileInfo, TimesheetEntryForm, loan_personal_info_form
from .models import TimesheetEntry, loan_personal_info

#Login stuff
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'base.html')

def register(request):
    
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                
            profile.save()
            
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        
    return render(request, 'chore_site/registration.html',
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':registered})
    
@login_required
def user_logout(request):
     logout(request)
     return HttpResponseRedirect(reverse('home'))


#Login view
def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('Account not active')
        else:
            print('Someone tried to login and failed')
            print(f'Username:{username} and password {password}')
            return HttpResponse('Invalid login details provided')
    else:
        return render(request, 'chore_site/login.html',{})
    

#Timesheet view
@login_required
def submit_timesheet(request):
    user_name = request.user
    
    if request.method == 'POST':
        form = TimesheetEntryForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        form = TimesheetEntryForm()
        
    entries = TimesheetEntry.objects.filter(user=request.user)
    return render(request, 'chore_site/timesheet.html', {'entries': entries,
                                              'form':form,
                                              'user_name':user_name})
    

def loan_application(request):
    user_name = request.user
    
    if request.method == 'POST':
        loan_application_form = loan_personal_info_form(request.POST)
        if loan_application_form.is_valid():
            instance = loan_application_form.save(commit=False)
            instance.user = request.user
            instance.save()
            
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        loan_application_form = loan_personal_info_form()
    
    loans = loan_personal_info.objects.filter(user=request.user)

    return render(request, 'chore_site\loan_application.html', {'user_name':user_name,
                                                                'loans':loans,
                                                                'loan_application_form':loan_application_form,
                                                                })
    

    


