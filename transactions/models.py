from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
from django.core.exceptions import ValidationError


class Transaction(models.Model):

    TRANSACTION_TYPE = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPE
    )

    description = models.CharField(
        max_length=255,
        blank=True
    )

    date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.amount} - {self.category}"
    
    def clean(self):
        if self.user_id != self.category.user_id:
            raise ValidationError(
                    {"category": "Category's user must be the same as the transaction's user."}
                )
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)