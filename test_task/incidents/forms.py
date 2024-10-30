from django import forms
from .models import Incident  # Импортируйте вашу модель инцидента

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = [
            'incident_date',
            'incident_time',
            'municipality',
            'settlement',
            'incident_type',
            'affected_houses',
            'restoration_date',
        ]
    
    def clean_incident_date(self):
        date = self.cleaned_data.get('incident_date')
        if not date:
            raise forms.ValidationError("Введите корректную дату.")
        return date

    def clean_restoration_date(self):
        date = self.cleaned_data.get('restoration_date')
        if not date:
            raise forms.ValidationError("Введите корректную дату.")
        return date
