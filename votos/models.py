# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Distrito(models.Model):
    """
    Se decide utilizar este modelo para la clase distrito porque es
    necesario el nombre y la cantidad de votantes,
    y en un futuro se mostrara un mapa con un marker por cada distrito
    que contenga los resultados del mismo.
    """
    nombre = models.CharField('Nombre del distrito', max_length=128)
    cantidad_votantes = models.IntegerField('Cantidad de votantes', default=0)
    latitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)
    longitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)


    def __str__(self):
        return 'Distrito {}'.format(self.nombre)

class Candidato(models.Model):
    """
    Cree variable nombre con un maximo de 50 caracteres
    , con valor por default Nombre candidato, y ademas tiene edad con valor por default 0
    """
    nombrec = models.CharField(max_length=50, default='Nombre candidato')
    edadc = models.IntegerField(default='0')
    #esta funcion define el nombre del objeto que aparecera en el admin 
    def __str__(self):
        return 'Candidato {}'.format(self.nombrec)


class Votos(models.Model):
    """
    Aca cree dos foreign Keys para definir que el voto contiene un candidato y un distrito.
    """
    candidatov = models.ForeignKey(Candidato)
    voto = models.IntegerField(null=True)
    distritov = models.ForeignKey(Distrito)

    def __str__(self):
        return 'voto para {}'.format(self.candidatov)