from django import forms
from .models import MeatSetting


class MeatForm(forms.ModelForm):
    class Meta:
        model = MeatSetting
        fields = ('plot_type',)
