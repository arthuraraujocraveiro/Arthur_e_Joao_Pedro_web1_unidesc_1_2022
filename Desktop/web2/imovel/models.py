from django.db import models

# Create your models here.

class Imovel(models.Model):

    matricula_imo = models.CharField(max_length=100)
    rua_imo = models.CharField(max_length=100)
    cep_imo = models.CharField(max_length=100)
    bairro_imo = models.CharField(max_length=100)
    cidade_imo = models.CharField(max_length=100)
    uf_imo = models.CharField(max_length=100)
    tamanho_imo = models.CharField(max_length=100)
    comodos_imo = models.CharField(max_length=100)
    garagem_imo = models.CharField(max_length=100)
    valor_imo = models.CharField(max_length=100)
    tipo_imo = models.CharField(max_length=100)
    status_imo = models.CharField(max_length=100)

    def __str__(self):
        return self.incluir_anuncio

    def __str__(self):
        return self.consultar_anuncio

    def __str__(self):
        return self.alterar_anuncio

    def __str__(self):
        return self.remover_anuncio

