# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from passlib.hash import pbkdf2_sha256


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empresas(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')  # Field name made lowercase.
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

    class Meta:
        managed = False
        db_table = 'empresas'


class Usuarios(models.Model):

    username = models.CharField(max_length=35, blank=True, null=True)
    nome = models.CharField(unique=True,max_length=85, blank=True, null=True)
    email = models.CharField(unique=True, max_length=85, blank=True, null=True)
    senha = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'

    def verify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password, self.senha)