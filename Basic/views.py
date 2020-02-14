from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,UpdateView,CreateView
from.models import Events
from.models import User
# Create your views here.


class EventListView(ListView):
    model = Events
    context_object_name = 'events'
    template_name = "events/list.html"
    def get_queryset(self):
        queryset = self.request.user.events.all()
        return queryset


class EventCreateView(CreateView):
    model = Events
    template_name = 'events/create.html'

    def form_valid(self, form):

        event = form.save(commit=False)
        event.owner = self.request.user

        event.save()
        messages.success(self.request, 'The quiz was created with success! Go ahead and add some questions now.')
        return redirect('update', event.pk)

    def post(self, request, *args, **kwargs):

        return super().post(request, *args, **kwargs)


class EventUpdateView(UpdateView):
    model = Events
    fields = ('title', 'description', 'thumbnail', 'features', 'category', 'price',)
    template_name = 'events/create.html'

    def form_valid(self, form):
        event = form.save(commit=False)
        event.owner = self.request.user
        event.save()
        messages.success(self.request, 'The quiz was created with success! Go ahead and add some questions now.')
        return redirect('update', event.pk)