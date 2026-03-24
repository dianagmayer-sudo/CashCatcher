from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


"""
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["age", "occupation"]
"""

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

"""
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["age", "occupation"]
"""

class RegisterForm(UserCreationForm):

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    age = forms.IntegerField(required=False)
    occupation = forms.CharField(required=False)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]