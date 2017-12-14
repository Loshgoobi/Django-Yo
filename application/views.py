from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
from application.forms import ContactForm
from application.models import Player


class CreateNewUser(CreateView):
    model = Player
    fields = '__all__'

class UpdateUser(UpdateView):
    model = Player
    fields = ['username','password',]


class LoginView(TemplateView):

  template_name = 'front/Index.html'

  def post(self, request, **kwargs):

    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )

    return render(request, self.template_name)


class LogoutView(TemplateView):

  template_name = 'front/Index.html'

  def get(self, request, **kwargs):

    logout(request)

    return render(request, self.template_name)

def newUser(request, pk):

  newUser_inst = get_object_or_404(Player, pk=pk)

  # If this is a POST request then process the Form data
  if request.method == 'POST':
      form = ContactForm(request.POST)

      # Check if the form is valid:
      if form.is_valid():
          # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
          newUser_inst.firstname = form.cleaned_data['firstname']
          newUser_inst.lastname = form.cleaned_data['lastname']
          newUser_inst.username = form.cleaned_data['username']
          newUser_inst.password = form.cleaned_data['password']
          newUser_inst.save()

          # redirect to a new URL:
          return HttpResponseRedirect('front/Index.html')

          # If this is a GET (or any other method) create the default form.
      else:
          return HttpResponseRedirect('djangoyo/Error_connexion.html')

      return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst': book_inst})