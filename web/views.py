from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product
from .forms import ContactForm

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.urls import reverse

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def home(request):
    return render(request, 'web/index.html')

def servicios(request):
    return render(request, 'web/servicios.html')

def bicicleta(request):
    return render(request, 'web/bicicleta.html')

def patinete(request):
    return render(request, 'web/patinete.html')

def electrifica(request):
    return render(request, 'web/electrifica.html')

class ProductList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'web/ocasion.html'

class ProductDetail(DetailView):
    model = Product
    context_object_name = 'products'
    template_name = 'web/ocasion-detalle.html'

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            email_body = render_to_string('web/contacto_email.html', {'name': name, 'email': email, 'message': message})

            subject = 'Nuevo mensaje de contacto'
            from_email = 'avilabikesbcn@gmail.com'
            to_email = [email, 'avilabikesbcn@gmail.com']

            email_message = EmailMultiAlternatives(subject, strip_tags(email_body), from_email, to_email)
            email_message.attach_alternative(email_body, "text/html")
            email_message.send()
            messages.success(request, '¡Gracias por tu mensaje! Nos pondremos en contacto contigo pronto.')
            return redirect('web:contacto_exitoso')
        else:
            messages.error(request, 'Hubo un error en el formulario. Por favor, corrige los errores e intenta de nuevo.')
    else:
        form = ContactForm()

    return render(request, 'web/contacto.html', {'form': form})


def contacto_exitoso(request):
    return render(request, 'web/contacto_exitoso.html')

def politica(request):
    return render(request, 'web/politica.html')