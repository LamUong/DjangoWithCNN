from django import forms
from django.db import models

class ImageUploadForm(forms.Form):
    image = forms.ImageField()