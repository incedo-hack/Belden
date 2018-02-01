# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
from models import plugins
from tables import TableView, analysis_table_view
from django_tables2 import RequestConfig
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import UploadFileForm, add_new_plugin_form
import uuid
import os
from IssueDBQuery import findMatchingRulesFromLog

def index(request):
    return render(request, 'base.html')

def add_new_plugin(request):

    if request.method == 'POST':
        form = add_new_plugin_form (request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('All Rules'))
    else:
        form = add_new_plugin_form ()
    return render(request, 'add_new_rule.html', {'form': form})

def view_rules(request):
    table = TableView(plugins.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'tables.html', {'table': table})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            data = handle_uploaded_file(request.FILES['file'])
            table = analysis_table_view(data, template_name='django_tables2/bootstrap-responsive.html')
            RequestConfig(request).configure(table)
            return render(request, 'analysis_report.html', {'table': table})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    tmp_dir_name = "temp"
    fname = os.path.join(tmp_dir_name, uuid.uuid4().hex)
    if not os.path.exists(tmp_dir_name):
        os.makedirs(tmp_dir_name)
    with open(fname, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    #findMatchingRulesFromLog(fname,)

    data = []
    return data


