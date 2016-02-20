from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    
class RegisterForm(forms.Form):
    fl_name = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'name', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'name'"}))
    email = forms.EmailField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'email address', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'email address'"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'password'"}), label='')
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'confirm password', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'confirm password'"}), label='')