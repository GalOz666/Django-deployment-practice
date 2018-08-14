from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', "email", "password")


class ProfileForm(forms.ModelForm):
    # website = form.URLField(blank=True)
    # profile_pic = form.ImageField(upload_to='profiles',blank=True, null=True)

    class Meta:
        model = UserProfile
        fields = ('website', 'profile_pic')

