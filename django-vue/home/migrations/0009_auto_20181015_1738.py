# Generated by Django 2.1 on 2018-10-15 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20181015_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeCreditos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField(blank=True, null=True)),
                ('is_active', models.IntegerField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(blank=True, null=True)),
                ('creditos', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'home_creditos',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='creditos',
            options={'managed': False},
        ),
    ]
