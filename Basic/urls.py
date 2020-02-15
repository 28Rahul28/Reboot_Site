from django.urls import path,include
from .Views import site, provider
from . import views
from allauth.account.views import SignupView

urlpatterns = [
    path('', views.Homeview.as_view(), name='Home'),
    path('search/', views.SearchView.as_view(), name='search_results'),
    path('accounts/signup/', site.Signup.as_view(), name='Signup'),
    path('accounts/signup/tourist/', SignupView.as_view(), name = 'Tourist_signup'),
    path('accounts/signup/service/', provider.Service, name='Service'),
    path('accounts/', include('allauth.urls')),
    path('events/list/', views.EventListView.as_view() ,name = 'list'),
    path('events/create/', views.EventCreateView.as_view(), name ='create'),
    path('events/update/<int:pk>/', views.EventUpdateView.as_view(), name = 'update'),
    path('events/delete/<int:pk>/', views.EventDeleteView.as_view(), name ='delete'),
    path('event/view/<int:pk>/', views.EventDetailView.as_view(), name = 'view'),

    path('api/search/', views.EventAPIView),
    ]