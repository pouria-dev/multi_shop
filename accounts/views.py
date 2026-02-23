from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import authenticate , login
from .form import Login_Form



class Login_View(FormView):
    template_name = 'accounts/login.html'
    form_class = Login_Form
    success_url = reverse_lazy("home:home")

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = authenticate(username=email , password=password)
        if user is not None:
            login(self.request , user)
            
        else:
            form.add_error("email" , "user dosen't exists")
            form.add_error("password" , "password is incorrect")
            return self.form_invalid(form)
            

        return super().form_valid(form)
    