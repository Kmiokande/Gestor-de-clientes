from django.urls import path
from clientes.views import persons_list
from clientes.views import person_new
from clientes.views import person_update

urlpatterns = [
    path('list/', persons_list, name='persons_list'),
    path('new/', person_new, name='person_new'),
    path('update/<int:id>', person_update, name='person_update'),
]
