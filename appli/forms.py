from django.forms import Form, EmailInput, Textarea
from django import forms


class Mail(Form):
    mail = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=Textarea, required=True)
