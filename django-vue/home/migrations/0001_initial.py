# Generated by Django 2.1.2 on 2018-10-02 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('cnpj', models.CharField(blank=True, db_column='CNPJ', max_length=18, null=True)),
                ('matrizfilial', models.CharField(blank=True, max_length=6, null=True)),
                ('abertura', models.CharField(blank=True, db_column='ABERTURA', max_length=10, null=True)),
                ('nm', models.CharField(blank=True, db_column='NM', max_length=155, null=True)),
                ('nmf', models.CharField(blank=True, db_column='NMF', max_length=60, null=True)),
                ('porte', models.CharField(blank=True, max_length=10, null=True)),
                ('nj', models.CharField(blank=True, db_column='NJ', max_length=100, null=True)),
                ('lg', models.CharField(blank=True, db_column='LG', max_length=80, null=True)),
                ('nr', models.CharField(blank=True, db_column='NR', max_length=10, null=True)),
                ('cp', models.CharField(blank=True, db_column='CP', max_length=150, null=True)),
                ('cep', models.CharField(blank=True, db_column='CEP', max_length=10, null=True)),
                ('br', models.CharField(blank=True, db_column='BR', max_length=80, null=True)),
                ('mu', models.CharField(blank=True, db_column='MU', max_length=40, null=True)),
                ('uf', models.CharField(blank=True, db_column='UF', max_length=2, null=True)),
                ('situacao', models.CharField(blank=True, db_column='SITUACAO', max_length=60, null=True)),
                ('telefone', models.CharField(blank=True, db_column='TELEFONE', max_length=45, null=True)),
                ('enderecoeletronico', models.CharField(blank=True, db_column='EnderecoEletronico', max_length=55, null=True)),
                ('dtcaptura', models.DateTimeField(blank=True, null=True)),
                ('efr', models.CharField(blank=True, max_length=45, null=True)),
                ('dt_situacao', models.CharField(blank=True, max_length=45, null=True)),
                ('motivo_sit_cad', models.CharField(blank=True, max_length=85, null=True)),
                ('sit_esp', models.CharField(blank=True, max_length=85, null=True)),
                ('dtsit_esp', models.CharField(blank=True, max_length=45, null=True)),
                ('doc', models.BigIntegerField(blank=True, null=True)),
                ('ativa', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'empresas',
                'managed': False,
            },
        ),
    ]
