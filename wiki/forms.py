from django import forms
from .models import Content
from django_summernote.widgets import SummernoteWidget
from django_summernote.fields import SummernoteTextFormField


class ContentModelForm(forms.ModelForm):
    class Meta:
        model = Content
        fields =[
            'title',
            'content',
            'image',
        ]
        widgets = {
            # 'content': SummernoteWidget()
            'content': SummernoteTextFormField()
        }
