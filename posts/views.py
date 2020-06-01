from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Image

# Create your views here.


class PostListView(LoginRequiredMixin,ListView):
    model = Image
    template_name= 'home.html'
    login_url = 'login'


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Image
    template_name = 'post_create.html'
    fields = ['image', 'name', 'caption']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)