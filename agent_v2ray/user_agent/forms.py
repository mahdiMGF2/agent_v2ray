from django import forms
from .models import User

class Loginfrom(forms.Form):
    username = forms.CharField(max_length=200,required=True)
    password = forms.CharField(widget=forms.PasswordInput,required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            try:
                user = User.objects.get(username=username)
                if not user.check_password(password):
                    raise forms.ValidationError("رمز عبور صحیح نیست")
            except User.DoesNotExist:
                raise forms.ValidationError("شما هنوز ثبت نام نکرده اید")

class Registerfrom(forms.Form):
    username = forms.CharField(max_length=200,required=True)
    password = forms.CharField(widget=forms.PasswordInput,required=True)

    def clean_username(self):
        username = self.cleaned_data['username']
        exitscheck = User.objects.filter(username=username)
        if exitscheck:
            raise forms.ValidationError("این نام کاربری استفاده شده است")
        else:
            return username