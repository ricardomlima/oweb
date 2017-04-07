from django.shortcuts import render
from django.http import HttpResponse
from documents.models import Document
from django import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from documents.models import Document
from django.views.generic import CreateView, ListView

class DocumentCreate(CreateView):
    model = Document
    fields = '__all__'
    template_name = 'create_document.html'
    success_url = reverse_lazy('index')

class Form_document(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'

def page(request):
    if len(request.POST) > 0:
        form = Form_document(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'create_document.html', {'form':form})
    else:
        form = Form_document()
        return render(request, 'create_document.html', {'form':form})