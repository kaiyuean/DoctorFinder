from django import forms
from localflavor.us.forms import USStateSelect, USZipCodeField
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from gmapi.forms.widgets import GoogleMap
from .models import Doctor, Insurance, User, Review

class SearchForm(forms.Form):
    speciality = forms.ChoiceField(widget=forms.Select, choices=Doctor.SPECIALITY_CHOICES)
    city = forms.CharField(max_length = 100)
    state = forms.CharField(widget = USStateSelect, max_length = 100)
    zip = USZipCodeField()
    insurance = forms.ChoiceField(widget = forms.Select, choices = Insurance.INSURANCE_CHOICES)

class SetSortForm(forms.Form):
    CHOICES = (('Rating', 'Rating'), ('Availability','Availability'))
    choice_field = forms.ChoiceField(widget=forms.RadioSelect(attrs={'onclick':'this.form.submit();'}), choices = CHOICES, label='Sort by')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'comment')

class SignUpForm(forms.ModelForm):   
    class Meta:
        model = User
        fields = ['username', 'name', 'password']
    confirm_password = forms.CharField(max_length = 100)

    #custom clean implementation to make sure passwords match
    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise ValidationError('Passwords must match')
        return self.cleaned_data

class LoginForm(forms.Form):
    username = forms.EmailField()
    password = forms.CharField(max_length=256)

    def clean(self):
        try:
            user = User.objects.get(username=self.cleaned_data['username'])
        except ObjectDoesNotExist:
            raise ValidationError('Username is invalid')
        if self.cleaned_data['password']!= user.password:
            raise ValidationError('Password is invalid')

class EditPatProForm(forms.ModelForm):   
    class Meta:
        model = User
        fields = ['username', 'name', 'password']
    confirm_password = forms.CharField(max_length = 100)

    #custom clean implementation to make sure passwords match
    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise ValidationError('Passwords must match')
        return self.cleaned_data

class EditDocProForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['phoneNumber', 'officeHours', 'speciality', 'availability', 'street', 'state', 'city', 'zip', 'education', 'awards', 'experience']


class MapForm(forms.Form):
    map = forms.Field(widget=GoogleMap(attrs={'width':500, 'height':500}))
