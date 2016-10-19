from django import forms
from member.models import MyUser
from django.contrib.auth import password_validation


class SignupModelForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
                'style': 'color: red;',
            }
        ),
        max_length=30,
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = MyUser
        fields = (
            'email',
            'password1',
            'password2',
            'last_name',
            'first_name',
            'nickname',
        )
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        # 'clean_ + 변수명' 함수는 해당 속성을 검증한다.

        # 여기 이해 안하셔도 됩니다
        # 비밀번호 같은지 & 비밀번호만의 유효성검사 루틴
        # https://docs.djangoproject.com/en/1.10/topics/auth/passwords/
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        password_validation.validate_password(
            self.cleaned_data['password2'],
            self.instance
        )
        return password2

    def save(self, commit=True):
        user = super(SignupModelForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.save()
        return user




class SignupForm(forms.Form):
    # https://docs.djangoproject.com/en/1.10/topics/forms/modelforms/
    # abcd = forms.ChoiceField(
    #     choices = (
    #         ('A', 'Apple'),
    #         ('B', 'Banana'),
    #     )
    # )
    email = forms.EmailField(
        max_length=100,
        error_messages={
            'invalid': '이메일 형식이 아닙니다',
        },
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    last_name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    first_name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    nickname = forms.CharField(
        max_length=24,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
