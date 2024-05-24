from django import forms
from django_recaptcha.fields import ReCaptchaField

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    captcha = ReCaptchaField(required=True)
