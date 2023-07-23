from django import forms

from .models import CustomersForm


class CreateForm(forms.ModelForm):
    class Meta:
        model = CustomersForm
        fields = '__all__'
