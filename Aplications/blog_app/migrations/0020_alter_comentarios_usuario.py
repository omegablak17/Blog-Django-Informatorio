# Generated by Django 4.0 on 2021-12-17 21:22

import Aplications.blog_app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0019_alter_comentarios_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='usuario',
            field=models.ForeignKey(blank=True, default=Aplications.blog_app.models.Usuarios, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog_app.usuarios'),
        ),
    ]
