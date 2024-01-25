from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        error_messages={'required': 'enter the pass plz'})
    
    password2 = forms.CharField(
        label='reEnter password',
        widget=forms.PasswordInput)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
           raise forms.ValidationError('Password does not match')
        return cd['password2']

    class Meta:
      model = User
      fields = ('username', 'first_name', 'email')
      help_texts = {'username': 'Только буквы, цифры и символы @.+-_'}
      verbose_name = {'username': 'login'}
      labels = {
         'username': 'Логин',
         'first_name' : 'Имя пользователя',
         'email' : 'эл.почта'
      }
      widgets = {
         'username': forms.TextInput,
         'email' : forms.EmailInput,
         'first_name' : forms.TextInput
      }

