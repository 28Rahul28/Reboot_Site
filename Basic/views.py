from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.views.generic import ListView,UpdateView,CreateView,DeleteView,DetailView
from.models import Events
from.forms import EventCreateForm, BookCreateForm
from django.contrib.auth.decorators import login_required
from.models import User
from django.utils.decorators import method_decorator
from.decorators import verified, user_is_entry_author
from django.db.models import Q
from .models import categories,Booking
# Create your views here.

class Homeview(ListView):
    model = Events
    template_name = 'account/home.html'
    context_object_name = 'list'
    def get_queryset(self):

        result = Events.objects.all()
        return result


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
                    Q(keywords__icontains=query) | Q(location__icontains=query) | Q(price__icontains=query))

        result = Events.objects.filter(or_lookup)
        print(result)
        return result

@method_decorator([verified],name='dispatch')
class EventListView(ListView):
    model = Events
    context_object_name = 'events'
    template_name = "events/list.html"
    def get_queryset(self):
        queryset = self.request.user.events.all()
        return queryset

@method_decorator([verified],name='dispatch')
class EventCreateView(CreateView):
    model = Events
    template_name = 'events/create.html'
    form_class = EventCreateForm
    def form_valid(self, form):

        events = form.save(commit=False)
        events.owner = self.request.user
        events.thumbnail = self.request.FILES['thumbnail']
        events.save()
        return super(EventCreateView, self).form_valid(form)
    def get_success_url(self):
        return reverse('list')

@method_decorator(login_required, name='dispatch')
class BookCreateView(CreateView):
    model = Booking
    template_name = 'booking/create.html'
    form_class = BookCreateForm
    def form_valid(self, form):

        Bookings = form.save(commit=False)
        Bookings.user = self.request.user
        Bookings.save()
        return super(BookCreateView, self).form_valid(form)
    def get_success_url(self):
        return reverse('book_list')

    def get_context_data(self, *args, **kwargs):
        context = super(BookCreateView, self).get_context_data(*args, **kwargs)
        context['event'] = Events.objects.get(pk=self.kwargs.get('pk'))
        return context
class BookListView(ListView):
    model = Booking
    context_object_name = 'events'
    template_name = "booking/list.html"
    def get_queryset(self):
        queryset = self.request.user.bookings.all()
        return queryset

class BookDeleteView(DeleteView):
    model = Booking
    template_name = "boooking/confirm_delete.html"

    def get_success_url(self):
        return reverse('booklist')

@method_decorator([verified],name='dispatch')
class EventUpdateView(UpdateView):
    model = Events
    fields = ('title', 'description', 'thumbnail', 'keywords', 'price',)
    template_name = 'events/create.html'

    def form_valid(self, form):
        event = form.save(commit=False)
        if event.owner != self.request.user:
            messages.success(message="Permission Denied",request=self.request)
            return redirect('list')
        event.save()
        messages.success(self.request, 'The quiz was created with success! Go ahead and add some questions now.')
        return redirect('update', event.pk)



@method_decorator([verified],name='dispatch')
class EventDeleteView(DeleteView):
    model = Events
    template_name = "events/confirm_delete.html"

    def get_success_url(self):
        return reverse('list')

class EventDetailView(DetailView):

    template_name = "events/service-details.html"
    model = Events

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


#rest api
from rest_framework import generics
from rest_framework import filters
from .models import Events
from .serializers import EventSerializer


class EventAPIView(generics.ListCreateAPIView):
    search_fields = ['title', 'description', 'category','price']
    filter_backends = (filters.SearchFilter,)
    queryset = Events.objects.all()
    serializer_class = EventSerializer
