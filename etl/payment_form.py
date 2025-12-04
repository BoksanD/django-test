from .models import Payment
from django import forms



class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'paid_at']
        widgets = {
            'paid_at': forms.DateTimeInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            # Disable localization so Django doesn't turn it into dd.mm.yyyy
            self.fields['paid_at'].localize = False

            # Accept the correct HTML5 date format
            self.fields['paid_at'].input_formats = ['%Y-%m-%d']

