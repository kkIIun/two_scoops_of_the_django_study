from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

class SignInForm(forms.Form):
    username = forms.CharField(max_length=32, label="아이디",
        error_messages={
            'required' : "아이디를 입력하세요"
        })
    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput,
        error_messages={
            'required' : "비밀번호를 입력하세요"
        })

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
        if username and password :
            user = User.objects.get(username=username)

            if not check_password(password,user.password) :
                self.add_error('password','비밀번호가 틀렸습니다.')
        
        return cleaned_data


class SignUpForm(UserCreationForm) :

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['phone'].required = True
        # self.fields['address'].required = True

    class Meta:
        model = User
        fields = ['username','password1','password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2 :
            self.add_error('password_confirm','비밀번호가 일치하지 않습니다.')