from django import forms
from django.forms import widgets
from .models import Trade

class TradeForm(forms.ModelForm):
    class Meta:
        model = Trade
        fields = ['direction', 'entry', 'take_profit',
                   'stop_loss', 'notes', 'image', 'entry_time',
                   'exit_time']
        widgets = {
            'entry_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'exit_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        } 
