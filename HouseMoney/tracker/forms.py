from django import forms
from .models import Payment, Log


class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ['name', 'notes', 'value', 'proof']


class LogForm(forms.ModelForm):

    class Meta:
        model = Log
        fields = ['value', 'utility', 'time']
