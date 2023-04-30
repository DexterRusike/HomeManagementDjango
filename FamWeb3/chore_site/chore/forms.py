from django import forms 
from django.contrib.auth.models import User
from chore.models import UserProfileInfo, TimesheetEntry, loan_personal_info

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)
        
class TimesheetEntryForm(forms.ModelForm):
    class Meta:
        model = TimesheetEntry
        fields = ['date', 'hours','activity','assigned_day']
        
class loan_personal_info_form(forms.ModelForm):
    class Meta:
        model = loan_personal_info
        fields = ['address','date_of_birth','home_number','mobile_number','amount','repayment','amount_due']
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': '36 fairwater Drive'}),
            'date_of_birth': forms.TextInput(attrs={'placeholder': '06/12/1999'}),
            'home_number': forms.TextInput(attrs={'placeholder': '+44 4567 45678'}),
            'mobile_number': forms.TextInput(attrs={'placeholder': '+44 4567 45678'}),
            'amount': forms.TextInput(attrs={'placeholder': 'Enter amount'}),
            'repayment': forms.TextInput(attrs={'placeholder': 'Enter repayment date'}),
            'amount_due': forms.TextInput(attrs={'placeholder': 'Enter amount due'})
        }
    

