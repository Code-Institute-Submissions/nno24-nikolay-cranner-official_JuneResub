from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    order_id = forms.CharField(label='order_id', widget=forms.TextInput(attrs={
        'class': 'order_id',
        'type': 'hidden',
        'value': ''
    }))
    order_items = forms.CharField(label='order_items', widget=forms.TextInput(attrs={
        'class': 'order_items',
        'type': 'hidden',
        'value': ''
    }))
    user_id = forms.CharField(label='user_id', widget=forms.TextInput(attrs={
        'class': 'user_id',
        'type': 'hidden',
        'value': ''
    }))
    grand_total = forms.DecimalField(label='grand_total', widget=forms.TextInput(attrs={
        'class': 'grand_total',
        'type': 'hidden',
        'value': 0.00
    }))
    transaction_date = forms.DateField(label='transaction_date', widget=forms.DateInput(attrs={
        'class': 'transaction_date',
        'type': 'hidden',
        'value': ''
    }))
    transaction_time = forms.TimeField(label='transaction_time', widget=forms.TimeInput(attrs={
        'class': 'transaction_time',
        'type': 'hidden',
        'value': ''
    }))


    class Meta:
        model = Order
        fields = [
            'order_id',
            'order_items',
            'user_id',
            'grand_total',
            'transaction_date',
            'transaction_time',
        ]