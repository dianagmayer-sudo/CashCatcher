from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Transaction
from .forms import TransactionForm
from django.views.generic import ListView


class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = "transactions/add_transaction.html"

    success_url = reverse_lazy("transactions_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs["user"] = self.request.user

        return kwargs
    

class TransactionListView(ListView):

    model = Transaction
    template_name = "transactions/transaction_list.html"
    context_object_name = "transactions"

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).order_by("-date")


class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = "transactions/transaction_update.html"

    success_url = reverse_lazy("transactions_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs["user"] = self.request.user

        return kwargs


class TransactionDeleteView(DeleteView):

    model = Transaction
    template_name = "transactions/transaction_delete.html"

    success_url = reverse_lazy("transactions_list")