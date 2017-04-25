from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from documents.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class CategoryCreate(CreateView):
    form_class = CategoryForm
    template_name = 'create_category.html'

    def form_valid(self, form):
            category_obj = form.save(commit=False)
            category_obj.owner = self.request.user
            category_obj.save()
            return HttpResponseRedirect(reverse('list_category'))

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        return super(CategoryCreate, self).dispatch(request, *args, **kwargs)

class CategoryList(ListView):
    model = Category
    template_name = 'list_categories.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset


class CategoryView(DetailView):
    model = Category
    template_name = "view_category.html"


class CategoryUpdate(UpdateView):
    model = Category
    template_name = "update_category.html"
    fields = '__all__'
    success_url = reverse_lazy('list_category')