from django.views.generic import TemplateView


class Homeview(TemplateView):
    template_name = 'account/home.html'


class Signup(TemplateView):
    template_name = 'account/presign.html'
