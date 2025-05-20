from django import forms
from .models import Client


class LoginForm(forms.Form):
    telegram_login = forms.CharField(
        label="Telegram Login",
        max_length=50,
        widget=forms.TextInput(
            attrs={"placeholder": "@username", "class": "form-control"}
        ),
    )

    def clean_telegram_login(self):
        login = self.cleaned_data["telegram_login"].strip().lower()
        if not login.startswith("@"):
            login = f"@{login}"

        if not Client.objects.filter(telegram_id=login).exists():
            raise forms.ValidationError("Пользователь с таким логином не найден")

        return login
