from .models import plugins
from django.forms import ModelForm
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

class add_new_plugin_form(ModelForm):
    class Meta:
        model = plugins
        fields = {'Product', 'BugID', 'RuleString', 'RCA'}
