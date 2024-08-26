from django.urls import path

from people.views.people_views import CreatePeople, DeletePeople, FindById, ListPeople, UpdatePeople

urlpatterns = [
    path('people/create/', CreatePeople.as_view(), name="Criar"),
    path('people/update/<uuid:pk>', UpdatePeople.as_view(), name="Atualizar"),
    path('people/list', ListPeople.as_view(), name="Listar"),
    path('people/delete/<uuid:pk>', DeletePeople.as_view(), name="Deletar"),
    path('people/find/<uuid:pk>', FindById.as_view(), name="Buscar pelo ID"),
]
