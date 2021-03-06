import graphene
from graphene_django.types import DjangoObjectType
from .models import Lead


class LeadType(DjangoObjectType):
    class Meta:
        model = Lead


class Query(object):
    all_lead = graphene.List(LeadType)

    def resolve_all_lead(self, info, **kwargs):
        return Lead.objects.all()
