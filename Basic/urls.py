from django.urls import path,include
from .Views import site, provider
from . import views

urlpatterns = [
    path('', site.Homeview.as_view(), name='Home'),
    path('accounts/signup', site.Signup.as_view(), name='Signup'),
    path('accounts/signup/service', provider.Service, name='Service'),
    path('accounts/', include('allauth.urls')),
    path('events/list/', views.EventListView.as_view() ,name = 'list'),
    path('events/create/', views.EventCreateView.as_view(), name ='create'),
    path('events/update/<int:pk>/', views.EventUpdateView.as_view(), name = 'update'),
    path('events/update/<int:pk>/', views.EventDeleteView.as_view(), name ='delete'),
    ]