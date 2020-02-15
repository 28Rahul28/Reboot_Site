from allauth.account.views import SignupView
from ..forms import BusinessSignupForm
from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,TemplateView

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
import os
from django.views import View
import datetime
from django.core import signing
from django.contrib import messages


class BusinessUserRegistrationView(SignupView):
    template_name = 'account/signup_organiser.html'
    form_class = BusinessSignupForm
    redirect_field_name = 'next'
    view_name = 'Service'
    success_url = None

    def get_context_data(self, **kwargs):
        ret = super(BusinessUserRegistrationView, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret


Service = BusinessUserRegistrationView.as_view()

