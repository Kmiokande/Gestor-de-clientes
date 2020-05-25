from django.urls import path
from clientes.views import persons_list
from clientes.views import person_new

urlpatterns = [
    path('list/', persons_list, name='person_list'),
    path('new/', person_new, name='person_new'),
]
