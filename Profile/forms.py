from django import forms
from controller import checkIfUsernameExists
from django.core.exceptions import ValidationError


class ProfileForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=30, required=True,
                                 widget=forms.TextInput)

    last_name = forms.CharField(label="Last Name", max_length=30, required=False,
                                widget=forms.TextInput)

    username = forms.CharField(label="Username", max_length=30, required=True,
                               widget=forms.TextInput)

    password = forms.CharField(label="Password", max_length=30, required=True,
                               widget=forms.TextInput)

    password_retype = forms.CharField(label="Retype Password", max_length=30, required=True,
                               widget=forms.TextInput)

    bio = forms.CharField(label="Bio", max_length=30, required=True,
                          widget=forms.TextInput)

    school = forms.CharField(label="School", max_length=30,  required=False,
                             widget=forms.TextInput)

    work = forms.CharField(label="Work", max_length=30,  required=False,
                           widget=forms.TextInput)

    location = forms.CharField(label="Location", max_length=30,  required=False,
                               widget=forms.TextInput)

    profile_picture = forms.ImageField(label="Profile Picture",  required=False)

    email = forms.EmailField(label="Email", max_length=30,  required=True,
                             widget=forms.TextInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if checkIfUsernameExists(username):
            raise ValidationError('Username already Exists')

        # Remember to always return the cleaned data.
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        password_retype = self.cleaned_data['password_retype']

        if not password == password_retype:
            raise ValidationError('Passwords do not match')

        return password

