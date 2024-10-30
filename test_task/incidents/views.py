from django.shortcuts import render, redirect, get_object_or_404
from .models import Incident
from .forms import IncidentForm
from django.contrib import messages

def incident_list(request):
    incidents = Incident.objects.filter(is_deleted=False)  # Только не удаленные инциденты
    return render(request, 'incidents/incident_list.html', {'incidents': incidents})

def add_incident(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incident_list')
    else:
        form = IncidentForm()
    return render(request, 'incidents/add_incident.html', {'form': form})

def edit_incident(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    if request.method == 'POST':
        form = IncidentForm(request.POST, instance=incident)
        if form.is_valid():
            form.save()
            return redirect('incident_list')
    else:
        form = IncidentForm(instance=incident)
    return render(request, 'incidents/edit_incident.html', {'form': form})

def delete_incident(request, pk):
    incident = get_object_or_404(Incident, id=pk)

    if request.method == 'POST':
        incident.is_deleted = True
        incident.comment = request.POST.get('comment', '')
        incident.save()
        return redirect('deleted_incidents') 

    return render(request, 'incidents/delete_incident.html', {'incident': incident})


def deleted_incidents(request):
    deleted_incidents = Incident.objects.filter(is_deleted=True)
    return render(request, 'incidents/deleted_incidents.html', {'deleted_incidents': deleted_incidents})