from django import forms
from . import models

class DetailForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "border border-gray-300 rounded-md px-4 py-2 w-full",
            }
        ),
    )
    age = forms.IntegerField(
        label="Age",
        widget=forms.NumberInput(
            attrs={
                "class": "border border-gray-300 rounded-md px-4 py-2 w-full",
            }
        ),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class": "border border-gray-300 rounded-md px-4 py-2 w-full",
            }
        ),
    )
    address = forms.CharField(
        label="Address",
        widget=forms.Textarea(
            attrs={
                "class": "border border-gray-300 rounded-md px-4 py-2 w-full",
                "rows": 3,
            }
        ),
    )

class DetailModelForm(forms.ModelForm):
    class Meta:
        model = models.Detail
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                "class": "border border-gray-300 rounded-md px-4 py-2 w-full",
            }),
            'age': forms.NumberInput(attrs={
                "class": "border border-gray-300 rounded-md px-4 py-2 w-full",
            }),
            'email': forms.EmailInput(attrs={
                "class": "border border-gray-300 rounded-md px-4 py-2 w-full",
            }),
            'address': forms.Textarea(attrs={
                "class": "border border-gray-300 rounded-md px-4 py-2 w-full",
                "rows": 3,
            }),
        }