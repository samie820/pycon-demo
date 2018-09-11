from person.models import Person, Post
from graphene import ObjectType, Node, Schema
# from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

class PersonNode(DjangoObjectType):

    class Meta:
        model = Person
        interfaces = (Node, )
        filter_fields = ['name', 'posts']


class PostNode(DjangoObjectType):

    class Meta:
        model = Post
        interfaces = (Node, )
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'person': ['exact'],
            'person__name': ['exact'],
        }

class Query(ObjectType):
    person = Node.Field(PersonNode)
    all_persons = DjangoFilterConnectionField(PersonNode)

    post = Node.Field(PostNode)
    all_posts = DjangoFilterConnectionField(PostNode)

schema = Schema(query = Query)
