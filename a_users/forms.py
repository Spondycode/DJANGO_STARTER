from django.forms import ModelForm
from django import forms
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ["user"]
        widgets = {
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "displayname" : forms.TextInput(attrs={"placeholder": "Add Displayname"}),
            "info" : forms.Textarea(attrs={"rows":3, "placeholder": "Add Information about you..."}),
        }