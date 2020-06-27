from django.forms import ModelForm
from django import forms
from first.models import photo_upload

class photo_form(ModelForm):
    class Meta:
        model = photo_upload
        fields = '__all__'