from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
import pycountry
from crm.models import Customer


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",
                             widget=forms.EmailInput(attrs={'class': "form-control", 'placeholder': "Your Email"}))
    first_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(
        attrs={'class': "form-control w-50", 'placeholder': "First Name", 'style': {'margin-right': '10px'}}))
    last_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(
        attrs={'class': "form-control w-50", 'placeholder': "Last Name"}))
    username = forms.CharField(label="",
                               widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Username"}))
    password1 = forms.CharField(label="",
                                widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "Password"}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': "form-control", 'placeholder': "Confirm Password"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __int__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or ' \
                                            'fewer. Letters, digits and @/./+/-/_ only.</small></span> '

        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too ' \
                                             'similar to your other personal information.</li><li>Your password must ' \
                                             'contain at least 8 characters.</li><li>Your password can\'t be a ' \
                                             'commonly used password.</li><li>Your password can\'t be entirely ' \
                                             'numeric.</li></ul> '

        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as ' \
                                             'before, for verification.</small></span> '


countries = pycountry.countries
code_name = {}
for country in countries:
    code_name[country.alpha_2] = country.name


class AddCustomerForm(forms.ModelForm):
    title = forms.ChoiceField(required=True, choices=[('Mrs', 'Mrs'), ('Mr.', 'Mr.'), ('Dr.', 'Dr'), ('Prof.', 'Professor')],
                              label="", widget=forms.Select(attrs={'class': "form-control w-50", 'placeholder': "Customer Title", "name": "title"}))
    email = forms.EmailField(required=True, label="",
                             widget=forms.EmailInput(attrs={'class': "form-control", 'placeholder': "Customer's Email", "name": "email"}))
    first_name = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(
        attrs={'class': "form-control w-50", 'placeholder': "Customer's First Name", "name": "first_name"}))
    last_name = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(
        attrs={'class': "form-control w-50", 'placeholder': "Customer's Last Name", "name": "last_name"}))
    phone = forms.CharField(required=True, max_length=15, label="",
                            widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Customer's Phone N°", "name":"phone"}))
    zipcode = forms.CharField(required=True, label="",
                              widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Zip Code", "name": "zipcode"}))
    address = forms.CharField(required=True, label="",
                              widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Customer's Address", "name": "address"}))
    city = forms.CharField(required=True, label="",
                           widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "City", "name": "city"}))
    region = forms.CharField(required=True, label="",
                             widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "State/Region", "name": "region"}))
    country = forms.ChoiceField(required=True, choices=[(name+", "+code, name) for code, name in code_name.items()], label="",
                                widget=forms.Select(attrs={'class': "w-50 form-group form-control", 'placeholder': "Country", "name": "country"}))
    description = forms.CharField(required=True, label="", max_length=150,
                                  widget=forms.Textarea(attrs={'class': "form-control", 'placeholder': "Customer's Description", "name": "description"}))

    class Meta:
        model = Customer
        exclude = ('user',)

    def __int__(self, *args, **kwargs):
        super(AddCustomerForm, self).__init__(*args, **kwargs)

        self.fields['email'].help_text = '<span class="form-text text-muted"><small>This email is already used. ' \
                                         'Please use another email.</small></span> '
