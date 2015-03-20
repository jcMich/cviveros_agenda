from django.views.generic import CreateView, ListView, UpdateView, RedirectView, FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Contacto, Grupo
from .form import ContactoForm, GrupoForm, LoginForm


# Create your views here.
class ContactoCreateView(CreateView):
    form_class = ContactoForm
    success_url = '/agenda/contactos'
    template_name = 'agenda/contacto_create.html'
    context_object_name = 'form'

    def get_form_kwargs(self):
        kwargs = super(ContactoCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        contacto = form.save(commit=False)
        contacto.owner = self.request.user
        contacto.save()
        return super(ContactoCreateView, self).form_valid(form)


class GrupoCreateView(CreateView):
    form_class = GrupoForm
    success_url = '/agenda/grupos'
    template_name = 'agenda/grupo_create.html'
    context_object_name = 'form'

    def form_valid(self, form):
        grupo = form.save(commit=False)
        grupo.owner = self.request.user
        grupo.save()
        return HttpResponseRedirect(reverse('grupos_list'))


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


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'agenda/login.html'
    success_url = '/agenda/contactos'

    def form_valid(self, form):
        user = form.cleaned_data.get('usuario')
        passw = form.cleaned_data.get('password')

        usuario = authenticate(username=user, password=passw)

        if usuario is not None and usuario.is_active:
            login(self.request, usuario)
        return super(LoginView, self).form_valid(form)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


class ContactoSearch(ListView):
    template_name = 'agenda/search.html'
    context_object_name = 'lista'
    model = Contacto
    http_method_names = ('get', 'post')

    def queryset(self):
        if 'search' in self.request.POST:
            search = self.request.POST.get('search')
        else:
            search = ''
        query = Contacto.objects.filter(owner=self.request.user).filter(nombre__contains=search)
        return query


class GrupoUpdateView(UpdateView):
    model = Grupo
    template_name = 'agenda/grupo_update.html'
    success_url = '/agenda/grupos'
    context_object_name = 'form'


class GrupoDeleteView(RedirectView):
    def get(self, request, *args, **kwargs):
        obj = Grupo.objects.get(pk=self.kwargs['pk'])
        obj.delete()
        return HttpResponseRedirect('/agenda/grupos')


class GrupoListView(ListView):
    model = Grupo
    template_name = 'agenda/grupos_list.html'
    context_object_name = 'list'

    # def get_queryset(self):
    #    query = Grupo.objects.filter(dueno=self.request.user).order_by('nombre')
    #    return query


contacto_create = login_required(ContactoCreateView.as_view(), login_url='/login')
grupo_create = login_required(GrupoCreateView.as_view(), login_url='/login')
contactos_list = login_required(ContactoListView.as_view(), login_url='/login')
contacto_update = login_required(ContactoUpdateView.as_view(), login_url='/login')
login_view = LoginView.as_view()
contacto_delete = login_required(ContactoDeleteView.as_view(), login_url='/login')
contacto_search = login_required(ContactoSearch.as_view())
grupo_update = login_required(GrupoUpdateView.as_view(), login_url='/login')
grupo_delete = login_required(GrupoDeleteView.as_view(), login_url='/login')
grupos_list = login_required(GrupoListView.as_view(), login_url='/login')