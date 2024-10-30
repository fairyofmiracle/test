# Generated by Django 5.1.2 on 2024-10-30 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0003_remove_incident_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='delete_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='incident',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
