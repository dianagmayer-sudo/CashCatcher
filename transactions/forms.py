from django import forms
from .models import Transaction
from categories.models import Category

class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction

        fields = [
            'amount',
            'category',
            'transaction_type',
            'description',
            'date'
        ]

        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'datepicker',
                }
            )
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        self.fields["category"].queryset = Category.objects.filter(
            user=user
        )