from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404
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
            try:
                user = get_object_or_404(User, username=username)
                if not check_password(password,user.password):
                    self.add_error('password','아이디 혹은 비밀번호가 틀렸습니다.')
            except:
                self.add_error('password','아이디 혹은 비밀번호가 틀렸습니다.')
        
        return cleaned_data


class SignUpForm(forms.Form) :
    username = forms.CharField(max_length=32, label="아이디",
        error_messages={
            'required' : "아이디를 입력하세요"
        })
    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput,
        error_messages={
            'required' : "비밀번호를 입력하세요"
        })
    confirm_password = forms.CharField(widget=forms.PasswordInput, label = '비밀번호확인',
        error_messages={
            'required' : "비밀번호확인을 입력하세요"
        })
    phone = forms.CharField(max_length=20)
    address = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].required = True
        self.fields['address'].required = True

    class Meta:
        model = User
        fields = ['username','password','confirm_password','phone','address']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('confirm_password')

        if password1 != password2 :
            self.add_error('confirm_password','비밀번호가 일치하지 않습니다.')