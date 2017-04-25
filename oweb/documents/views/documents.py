from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from documents.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['url', 'category']

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
        user = request.user
        return super(DocumentCreate, self).dispatch(request, *args, **kwargs)

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


def page(request):
    if len(request.POST) > 0:
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'create_document.html', {'form':form})
    else:
        form = DocumentForm()
        return render(request, 'create_document.html', {'form':form})