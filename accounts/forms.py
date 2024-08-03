from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Username or Email")

    def clean(self):
        cleaned_data = super().clean()
        username_or_email = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username_or_email and password:
            # Check if the input is an email
            if '@' in username_or_email:
                try:
                    user = User.objects.get(email=username_or_email)
                    cleaned_data['username'] = user.username
                except User.DoesNotExist:
                    # If email is not found, keep it as is (could be username)
                    cleaned_data['username'] = username_or_email
            else:
                cleaned_data['username'] = username_or_email

        return cleaned_data
