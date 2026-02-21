from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import authenticate , login
from .form import Login_Form , Register_Form



class Login_View(FormView):
    template_name = None
    form_class = Login_Form
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username , password=password)
        if user is not None:
            login(self.request , user)

        return super().form_valid(form)
    