import logging
from people.serializers.serializers import PeopleSerializer
from people.models.entity.people_models import People
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from asyncio.log import logger
from drf_yasg import openapi

# Defina o nível de logging como INFO ou DEBUG
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CreatePeople(generics.CreateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    @swagger_auto_schema(
        operation_description="Cria novo dado",
        tags=['People'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'nome': openapi.Schema(type=openapi.TYPE_STRING, description='Nome do Usuário', example='Robson Ferreira'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email do Usuário', example='rob@gmail.com'),
                'idade': openapi.Schema(type=openapi.TYPE_STRING, description='Idade do Usuário', example=30),
                'profissao': openapi.Schema(type=openapi.TYPE_STRING, description='Profissão do Usuário', example='Desenvolvedor'),
                'salario': openapi.Schema(type=openapi.TYPE_STRING, description='Salário do Usuário', example='5.000'),
            }
        ),
        responses={
            201: openapi.Response(
                description="Registro Criado com sucesso",
                examples={
                    'application/json': {
                        'message': 'Registro Criado com sucesso',
                        'data': {
                            "nome": "Robson Ferreira",
                            "email": "rob@gmail.com",
                            "idade": 30,
                            "profissao": "Desenvolvedor",
                            "salario": "5000.00"
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="Erro ao criar registro",
                examples={
                    'application/json': {
                        'message': 'Erro ao criar registro'
                    }
                }
            )
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class UpdatePeople(generics.UpdateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    @swagger_auto_schema(
        operation_description="Atualiza um Registro",
        tags=['People'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'nome': openapi.Schema(type=openapi.TYPE_STRING, description='Nome do Usuário', example='Robson Ferreira'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email do Usuário', example='rob@gmail.com'),
                'idade': openapi.Schema(type=openapi.TYPE_STRING, description='Idade do Usuário', example=30),
                'profissao': openapi.Schema(type=openapi.TYPE_STRING, description='Profissão do Usuário', example='Desenvolvedor'),
                'salario': openapi.Schema(type=openapi.TYPE_STRING, description='Salário do Usuário', example='5.000'),
            }
        ),
        responses={
            201: openapi.Response(
                description="Registro atualizado com sucesso",
                examples={
                    'application/json': {
                        'message': 'Registro Atualizado com sucesso',
                        'data': {
                            "nome": "Robson Ferreira",
                            "email": "rob@gmail.com",
                            "idade": 30,
                            "profissao": "Desenvolvedor",
                            "salario": "5000.00"
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="Erro ao atualizar registro",
                examples={
                    'application/json': {
                        'message': 'Erro ao atualizar registro'
                    }
                }
            )
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class ListPeople(generics.ListAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    @swagger_auto_schema(
        operation_description="Lista todos os registros",
        tags=['People'],
        responses={
            200: openapi.Response(
                description="Lista de registros",
                examples={
                    'application/json': {
                        'results': [
                            {
                                "count": 2,
                                "next": 10,
                                "previous": 1,
                                "results": [
                                    {
                                        "id": "34e7f785-c647-4552-a1c5-efc904ae9654",
                                        "nome": "Robson Ferreira",
                                        "email": "rob@gmail.com",
                                        "idade": 30,
                                        "profissao": "Desenvolvedor",
                                        "salario": "3000.00"
                                    },
                                    {
                                        "id": "03c1cf42-2bc9-4885-8e5b-29529031087c",
                                        "nome": "Robson Ferreira",
                                        "email": "rob@example.com",
                                        "idade": 30,
                                        "profissao": "Desenvolvedor",
                                        "salario": "3000.00"
                                    }
                                ]
                            }
                        ]
                    }
                }
            )
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class DeletePeople(generics.DestroyAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class FindById(generics.RetrieveAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
