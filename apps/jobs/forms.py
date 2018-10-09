

from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user', 'bio', 'location','birth_date')

    def save(self, commit=True):
        user = super(ProfileForm, self).save(commit=False)
        # user.first_name = self.cleaned_data['first_name']

        if commit:
            user.save()
        return user

