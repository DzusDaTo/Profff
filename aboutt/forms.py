from .models import Aboutt
from django.forms import ModelForm, TextInput, IntegerField


class AbouttForm(ModelForm):
    class Meta:
        model = Aboutt
        fields = ['zp', 'trebovan', 'bonus', 'navki', 'o_kompani', 'number', 'special']
        widgets = {
            "zp": TextInput(attrs={'placeholder': 'Заработная плата'}),
            "trebovan": TextInput(attrs={'class': 'form-control', 'placeholder': 'Требования'}),
            "bonus": TextInput(attrs={'class': 'form-control', 'placeholder': 'Бонусы'}),
            "navki": TextInput(attrs={'class': 'form-control', 'placeholder': 'Навыки'}),
            "o_kompani": TextInput(attrs={'class': 'form-control', 'placeholder': 'О кампании'}),
            "number": TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}),
            "special": TextInput(attrs={'class': 'form-control', 'placeholder': 'Специальность '}),
        }