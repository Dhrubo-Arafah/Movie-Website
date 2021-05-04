from django.contrib.auth.models import User
from django.forms import ModelForm, forms

from core.models import File, Profile


class ItemForm(ModelForm):
    class Meta:
        model = File
        fields = '__all__'


class EditProfile(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude=('user',)
