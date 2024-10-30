from django.db import models

class Incident(models.Model):
    incident_date = models.DateField(verbose_name="Дата происшествия")
    incident_time = models.TimeField(verbose_name="Время происшествия")
    municipality = models.CharField(max_length=100, verbose_name="Муниципальный район")
    settlement = models.CharField(max_length=100, verbose_name="Населенный пункт")
    incident_type = models.CharField(max_length=20, choices=[
        ('water', 'Вода'),
        ('heat', 'Тепло'),
        ('light', 'Свет'),
        ('gas', 'Газ'),
    ], verbose_name="Вид происшествия")
    affected_houses = models.IntegerField(verbose_name="Отключено домов")
    restoration_date = models.DateField(null=True, blank=True, verbose_name="Дата восстановления")
    is_deleted = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        incident_type_display = dict(self._meta.get_field('incident_type').choices).get(self.incident_type)
        return f"{incident_type_display} в {self.settlement} на {self.incident_date}"
