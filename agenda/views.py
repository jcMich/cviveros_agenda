from django.views.generic import CreateView, ListView, UpdateView, RedirectView
from .models import Contacto
# Create your views here.
from .form import ContactoForm, GrupoForm, ColorForm
from django.http import HttpResponseRedirect


class ContactoCreateView(CreateView):
    form_class = ContactoForm
    success_url = '/agenda/contactos'
    template_name = 'agenda/contacto_create.html'
    context_object_name = 'form'

    def form_valid(self, form):
        contacto = form.save(commit=False)
        contacto.owner = self.request.user
        contacto.save()
        return super(ContactoCreateView, self).form_valid(form)


class GrupoCreateView(CreateView):
    form_class = GrupoForm
    success_url = '/agenda/contactos'
    template_name = 'agenda/grupo_create.html'
    context_object_name = 'form'


class ColorCreateView(CreateView):
    form_class = ColorForm
    success_url = '/agenda/contactos'
    template_name = 'agenda/color_create.html'
    context_object_name = 'form'


class ContactoListView(ListView):
    model = Contacto
    template_name = 'agenda/contactos_list.html'
    context_object_name = 'list'

    def get_queryset(self):
        query = Contacto.objects.filter(owner=self.request.user).order_by('nombre')
        return query


class ContactoUpdateView(UpdateView):
    model = Contacto
    template_name = 'agenda/contacto_update.html'
    success_url = '/agenda/contactos'
    context_object_name = 'form'


class ContactoDeleteView(RedirectView):
    def get(self, request, *args, **kwargs):
        obj = Contacto.objects.get(pk=self.kwargs['pk'])
        obj.delete()
        return HttpResponseRedirect('/agenda/contactos')

contacto_create = ContactoCreateView.as_view()
grupo_create = GrupoCreateView.as_view()
contactos_list = ContactoListView.as_view()
contacto_update = ContactoUpdateView.as_view()
contacto_delete = ContactoDeleteView.as_view()
color_create = ColorCreateView.as_view()
