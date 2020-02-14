from django.urls import path, include
from.registration import urls

urlpatterns =[
    path('registration/', include(urls)),
    path('', include('rest_auth.urls')),

    
]