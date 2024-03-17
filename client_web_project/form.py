from django.forms import ModelForm
from client_web_project.models import *

class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ('word','imi')
