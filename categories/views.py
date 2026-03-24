from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category
from .forms import CategoryForm


class CategoryListView(ListView):

    model = Category
    template_name = "categories/category_list.html"
    context_object_name = "categories"

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class CategoryCreateView(CreateView):

    model = Category
    form_class = CategoryForm
    template_name = "categories/add_category.html"

    success_url = reverse_lazy("categories_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryUpdateView(UpdateView):

    model = Category
    form_class = CategoryForm
    template_name = "categories/category_update.html"

    success_url = reverse_lazy("categories_list")


class CategoryDeleteView(DeleteView):

    model = Category
    template_name = "categories/category_delete.html"

    success_url = reverse_lazy("categories_list")