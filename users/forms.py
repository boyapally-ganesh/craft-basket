from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class userregister(UserCreationForm):
       email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
       password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
       password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
       class Meta:
            model = User
            fields = ('username','email','password1','password2')
            widgets={
        'username':forms.TextInput(attrs={'class':'form-control'}),
        #'first_name':forms.TextInput(attrs={'class':'form-control'}),
        #'last_name':forms.TextInput(attrs={'class':'form-control'}),
      }
  
class usereditform(UserChangeForm):
      password = None
  
      class Meta:
        model = User
        fields = ('username','email','first_name','last_name')
        labels = {'email':'Email'}
