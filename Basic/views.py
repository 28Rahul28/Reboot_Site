from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.views.generic import ListView,UpdateView,CreateView,DeleteView,TemplateView
from.models import Events
from.forms import EventCreateForm
from.models import User
from django.utils.decorators import method_decorator
from.decorators import verified
from django.db.models import Q
# Create your views here.

def Homeview(ListView):
    model = Events


class SearchView(ListView):
    model = Events
    template_name = 'search/result.html'
    paginate_by = 20
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        or_lookup = []
        if query is not None:
            or_lookup = (Q(title__icontains=query) |Q(description__icontains=query) |
                    Q(features__icontains=query) | Q(location__icontains=query) | Q(price__icontains=query))

        result = Events.objects.filter(or_lookup)
        print(result)
        return result
            # just an empty queryset as default

@method_decorator([verified],name='dispatch')
class EventListView(ListView):
    model = Events
    context_object_name = 'events'
    template_name = "events/list.html"
    def get_queryset(self):
        queryset = get_object_or_404(self.request.user.events.all())
        return queryset

@method_decorator([verified],name='dispatch')
class EventCreateView(CreateView):
    model = Events
    template_name = 'events/create.html'
    form_class = EventCreateForm
    def form_valid(self, form):

        events = form.save(commit=False)
        events.owner = get_object_or_404(self.request.user)

        events.thumbnail = self.request.FILES['thumbnail']
        events.save()
        return super(EventCreateView, self).form_valid(form)
    def get_success_url(self):
        return reverse('list')




@method_decorator([verified],name='dispatch')
class EventUpdateView(UpdateView):
    model = Events
    fields = ('title', 'description', 'thumbnail', 'features', 'price',)
    template_name = 'events/create.html'

    def form_valid(self, form):
        event = form.save(commit=False)
        event.owner = self.request.user
        event.save()
        messages.success(self.request, 'The quiz was created with success! Go ahead and add some questions now.')
        return redirect('update', event.pk)

@method_decorator([verified],name='dispatch')
class EventDeleteView(DeleteView):
    model = Events
    template_name = "events/confirm_delete.html"

    def get_success_url(self):
        return reverse('list')
