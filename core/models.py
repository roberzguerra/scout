# -*- coding:utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

ACTIVE = 'Y'
INACTIVE = 'N'
CHOICE_ACTIVE = (
    ('Y', _(u"Sim")),
    ('N', _(u"Não")),
)

UF = (
    ('RS', _(u"Rio Grande do Sul"),),
    ('AC', _(u"Acre"),),
    ('AL', _(u"Alagoas"),),
    ('AP', _(u"Amapá"),),
    ('AM', _(u"Amazonas"),),
    ('BA', _(u"Bahia"),),
    ('CE', _(u"Ceará"),),
    ('DF', _(u"Distrito Federal"),),
    ('ES', _(u"Espírito Santo"),),
    ('GO', _(u"Goiás"),),
    ('MA', _(u"Maranhão"),),
    ('MT', _(u"Mato Grosso"),),
    ('MS', _(u"Mato Grosso do Sul"),),
    ('MG', _(u"Minas Gerais"),),
    ('PA', _(u"Pará"),),
    ('PB', _(u"Paraíba"),),
    ('PR', _(u"Paraná"),),
    ('PE', _(u"Pernambuco"),),
    ('PI', _(u"Piauí"),),
    ('RJ', _(u"Rio de Janeiro"),),
    ('RN', _(u"Rio Grande do Norte"),),
    ('RO', _(u"Rondônia"),),
    ('RR', _(u"Roraima"),),
    ('SC', _(u"Santa Catarina"),),
    ('SP', _(u"São Paulo"),),
    ('SE', _(u"Sergipe"),),
    ('TO', _(u"Tocantins"),),
)


class CoreModel(models.Model):
    """
    Model Padrao
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
