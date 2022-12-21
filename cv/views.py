from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from cv.models import *
from cv.froms import ContactoForm

# Create your views here.
class home(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['social_data'] = Social.objects.all()
        context['presentacion_data'] = Presentacion.objects.all()
        context['acercade_data'] = AcercaDe.objects.all()
        context['software_data'] = Software.objects.all()
        context['lenguajes_data'] = Lenguajes.objects.all()
        context['experiencia_data'] = Experiencia.objects.all()
        context['portafolio_data'] = Portafolio.objects.all()
        return context

class enviado(LoginRequiredMixin,TemplateView):
    template_name = 'enviado.html'

class ContactoView(LoginRequiredMixin,View):
    def get(self, request):
        form = ContactoForm()
        if Contacto.objects.filter(Usuario=request.user).exists():
            return render(request, 'error.html')
        else:
            return render(request, 'contacto.html', {'form': form})

    def post(self, request):
        form = ContactoForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.Usuario = request.user
            contact.save()
            return redirect('enviado')
