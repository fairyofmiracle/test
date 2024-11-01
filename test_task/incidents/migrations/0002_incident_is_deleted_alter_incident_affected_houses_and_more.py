# Generated by Django 5.1.2 on 2024-10-30 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Удалено'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='affected_houses',
            field=models.IntegerField(verbose_name='Отключено домов'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='incident_date',
            field=models.DateField(verbose_name='Дата происшествия'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='incident_time',
            field=models.TimeField(verbose_name='Время происшествия'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='incident_type',
            field=models.CharField(choices=[('water', 'Вода'), ('heat', 'Тепло'), ('light', 'Свет'), ('gas', 'Газ')], max_length=20, verbose_name='Вид происшествия'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='municipality',
            field=models.CharField(max_length=100, verbose_name='Муниципальный район'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='restoration_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата восстановления'),
        ),
        migrations.AlterField(
            model_name='incident',
            name='settlement',
            field=models.CharField(max_length=100, verbose_name='Населенный пункт'),
        ),
    ]
