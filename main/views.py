from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Gorev


class GirisYap(LoginView):
    template_name = 'main/giris.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('gorevler')


class GorevList(LoginRequiredMixin, ListView):
    model = Gorev
    context_object_name = 'gorevler'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gorevler'] = context['gorevler'].filter(kullanici=self.request.user)
        context['sayi'] = context['gorevler'].filter(bitis=False).count()
        arama_input = self.request.GET.get('arama') or ''
        if arama_input:
            context['gorevler'] = context['gorevler'].filter(baslik__icontains=arama_input)
            context['arama_input'] = arama_input
        return context

class KayitOl(FormView):
    template_name = 'main/kayit.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('gorevler')

    def form_valid(self, form):
        kullanici = form.save()
        if kullanici is not None:
            login(self.request, kullanici)
        return super(KayitOl, self).form_valid(form)
    
    def get (self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('gorevler')
        return super(KayitOl, self).get( *args, **kwargs)



class GorevDetay(LoginRequiredMixin, DetailView):
    model = Gorev
    context_object_name = 'gorev'
    template_name = 'main/gorev.html'

class GorevEkle(LoginRequiredMixin, CreateView):
    model = Gorev
    fields = ['baslik', 'aciklama', 'bitis']
    success_url = reverse_lazy('gorevler')

    def form_valid(self, form):
        form.instance.kullanici = self.request.user
        return super(GorevEkle, self).form_valid(form)

class GorevGuncelle(LoginRequiredMixin, UpdateView):
    model = Gorev
    fields = ['baslik', 'aciklama', 'bitis']
    success_url = reverse_lazy('gorevler')

class GorevSil(LoginRequiredMixin, DeleteView):
    model = Gorev
    context_object_name = 'gorev'
    template_name = 'main/gorev_silme_onay.html'        
    success_url = reverse_lazy('gorevler')
