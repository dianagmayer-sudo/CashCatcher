from django.views.generic import TemplateView
from transactions.models import Transaction
from django.db.models import Sum


class DashboardView(TemplateView):

    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        user = self.request.user

        income = Transaction.objects.filter(
            user=user,
            transaction_type="income"
        ).aggregate(Sum("amount"))["amount__sum"] or 0

        expenses = Transaction.objects.filter(
            user=user,
            transaction_type="expense"
        ).aggregate(Sum("amount"))["amount__sum"] or 0

        balance = income - expenses

        context["income"] = round(income, 2)
        context["expenses"] = round(expenses, 2)
        context["balance"] = round(balance, 2)

        return context