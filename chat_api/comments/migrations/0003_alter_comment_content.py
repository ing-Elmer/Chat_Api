# Generated by Django 3.2.19 on 2024-02-08 23:55

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_alter_comment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
