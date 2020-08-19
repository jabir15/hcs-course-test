from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='Enter first name', max_length=50)
    last_name = forms.CharField(label='Enter last name', max_length=50)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

    

    def save(self, commit=True):
        user=super(CustomUserCreationForm,self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['username']+'@hcs.com'
        if commit:
            user.save()
        return user