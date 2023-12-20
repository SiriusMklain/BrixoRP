from django import forms
from app2.models import VisitToTT, TextSlide
from django.utils import timezone
from django.forms.widgets import ClearableFileInput



class VisitToTTForm(forms.ModelForm):
    class Meta:
        model = VisitToTT
        fields = [
            'visits',
            'retail',
            'sto',
            'retail_buy_SAKURA_and_have',
            'sto_buy_SAKURA_and_have',
            'sto_dont_buy_SAKURA_and_have',
            'retail_dont_buy_SAKURA_and_have',
            'month',
        ]
        current_year = timezone.now().year
        # current_months = timezone.now().months
        widgets = {
            'visits': forms.TextInput(attrs={'class': 'form-control'}),
            'retail': forms.TextInput(attrs={'class': 'form-control'}),
            'sto': forms.TextInput(attrs={'class': 'form-control'}),
            'retail_buy_SAKURA_and_have': forms.TextInput(attrs={'class': 'form-control'}),
            'sto_buy_SAKURA_and_have': forms.TextInput(attrs={'class': 'form-control'}),
            'sto_dont_buy_SAKURA_and_have': forms.TextInput(attrs={'class': 'form-control'}),
            'retail_dont_buy_SAKURA_and_have': forms.TextInput(attrs={'class': 'form-control'}),
            'month': forms.DateInput(attrs={'class': 'form-control'}, format='%Y-%m'),
        }


class TextSlideForm(forms.ModelForm):
    class Meta:
        model = TextSlide
        fields = [
            'title',
            'text',
            'text_image',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'text_image': ClearableFileInput(attrs={'class': 'form-control'}),
        }