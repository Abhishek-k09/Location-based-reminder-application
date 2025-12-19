from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm password")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean(self):
        cleaned = super().clean()
        p = cleaned.get('password')
        c = cleaned.get('confirm')
        if p and c and p != c:
            raise forms.ValidationError("Passwords do not match")
        return cleaned
