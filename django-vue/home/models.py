
from django.db import models


class Empresas(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=18, blank=True, null=True)  # Field name made lowercase.
    matrizfilial = models.CharField(max_length=6, blank=True, null=True)
    abertura = models.CharField(db_column='ABERTURA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nm = models.CharField(db_column='NM', max_length=155, blank=True, null=True)  # Field name made lowercase.
    nmf = models.CharField(db_column='NMF', max_length=60, blank=True, null=True)  # Field name made lowercase.
    porte = models.CharField(max_length=10, blank=True, null=True)
    nj = models.CharField(db_column='NJ', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lg = models.CharField(db_column='LG', max_length=80, blank=True, null=True)  # Field name made lowercase.
    nr = models.CharField(db_column='NR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    br = models.CharField(db_column='BR', max_length=80, blank=True, null=True)  # Field name made lowercase.
    mu = models.CharField(db_column='MU', max_length=40, blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    situacao = models.CharField(db_column='SITUACAO', max_length=60, blank=True, null=True)  # Field name made lowercase.
    telefone = models.CharField(db_column='TELEFONE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    enderecoeletronico = models.CharField(db_column='EnderecoEletronico', max_length=55, blank=True, null=True)  # Field name made lowercase.
    dtcaptura = models.DateTimeField(blank=True, null=True)
    efr = models.CharField(max_length=45, blank=True, null=True)
    dt_situacao = models.CharField(max_length=45, blank=True, null=True)
    motivo_sit_cad = models.CharField(max_length=85, blank=True, null=True)
    sit_esp = models.CharField(max_length=85, blank=True, null=True)
    dtsit_esp = models.CharField(max_length=45, blank=True, null=True)
    doc = models.BigIntegerField(blank=True, null=True)
    ativa = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nm
    
    class Meta:
        #managed = False
        db_table = 'empresas'
