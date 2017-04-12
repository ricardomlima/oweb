"""oweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from documents.views import index, users, documents

urlpatterns = [
    url(r'^$', index.index, name="index"),
    url(r'^create-user$', users.page, name="create_user"),
    url(r'^create-document$',documents.DocumentCreate.as_view(),name = "create_document"),
    url(r'^list-documents$',documents.DocumentList.as_view(),name = "list_document"),
    url(r'^view-document/(?P<pk>\d+)$',documents.DocumentView.as_view(),name = "view_document"),
]
