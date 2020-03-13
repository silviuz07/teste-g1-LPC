# Generated by Django 3.0.3 on 2020-03-13 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_credencial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app_credencial.Pessoa')),
                ('cpf', models.TextField(max_length=11)),
            ],
            bases=('app_credencial.pessoa',),
        ),
    ]
