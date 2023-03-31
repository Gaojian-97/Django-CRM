from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '邮箱地址'}))
    first_name = forms.CharField(label="", max_length=20,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '姓'}))
    last_name = forms.CharField(label="", max_length=20,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '名'}))
    error_messages = {
        "password_mismatch": "两次密码输入不一致",
    }

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = '用户名'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = '<span class="form-text text-muted"><small>150 个字符或以下。用户名可包含字母数字、_、@、+、. 和 - ' \
                                    '字符</small></span> '

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = '密码'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too ' \
                                     'similar to your other personal information.</li><li>Your password must ' \
                                     'contain at least 8 characters.</li><li>Your password can\'t be a commonly ' \
                                     'used password.</li><li>Your password can\'t be entirely numeric.</li></ul> '

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = '确认密码'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as ' \
                                     'before, for verification.</small></span> '


# Create Add Record Form
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "First Name", "class": "form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Last Name", "class": "form-control"}), label="")
    email = forms.CharField(required=True,
                            widget=forms.widgets.TextInput(attrs={"placeholder": "Email", "class": "form-control"}),
                            label="")
    phone = forms.CharField(required=True,
                            widget=forms.widgets.TextInput(attrs={"placeholder": "Phone", "class": "form-control"}),
                            label="")
    address = forms.CharField(required=True,
                              widget=forms.widgets.TextInput(attrs={"placeholder": "Address", "class": "form-control"}),
                              label="")
    city = forms.CharField(required=True,
                           widget=forms.widgets.TextInput(attrs={"placeholder": "City", "class": "form-control"}),
                           label="")
    state = forms.CharField(required=True,
                            widget=forms.widgets.TextInput(attrs={"placeholder": "State", "class": "form-control"}),
                            label="")
    zipcode = forms.CharField(required=True,
                              widget=forms.widgets.TextInput(attrs={"placeholder": "Zipcode", "class": "form-control"}),
                              label="")

    class Meta:
        model = Record
        exclude = ("user",)
