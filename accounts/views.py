from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Create your views here.
class SignUpView(CreateView):
  
  form_class = CustomUserCreationForm
  
  template_name = "signup.html"
  
  success_url = reverse_lazy('accounts:signup_success')
  
  def form_valid(self, form):
    user = form.save()
    self.object = user
    
    return super().form_valid(form)
  
class SignUpSuccessView(TemplateView):
  
  template_name = "signup_success.html"

class LoginView(LoginView):
  template_name = 'login.html'
  
class LogoutView(LogoutView):
  template_name = 'login.html'