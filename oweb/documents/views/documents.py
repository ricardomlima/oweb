from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from documents.models import Document, Category


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['url', 'category']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(owner=user)


class DocumentCreate(CreateView):
    form_class = DocumentForm
    template_name = 'create_document.html'

    def form_valid(self, form):
            document_obj = form.save(commit=False)
            document_obj.owner = self.request.user
            document_obj.save()
            return HttpResponseRedirect(reverse('list_document'))

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(DocumentCreate, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(DocumentCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class DocumentList(ListView):
    model = Document
    template_name = 'list_documents.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = Document.objects.all()
        return queryset


class DocumentView(DetailView):
    model = Document
    template_name = "view_document.html"


class DocumentUpdate(UpdateView):
    model = Document
    template_name = "update_document.html"
    fields = '__all__'
    success_url = reverse_lazy('list_document')