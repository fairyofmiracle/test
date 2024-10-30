from django.urls import path
from .views import incident_list, add_incident, edit_incident, delete_incident, deleted_incidents

urlpatterns = [
    path('', incident_list, name='incident_list'),
    path('add_incident/', add_incident, name='add_incident'),
    path('edit/<int:pk>/', edit_incident, name='edit_incident'),
    path('incident/<int:pk>/delete/', delete_incident, name='delete_incident'),
    path('deleted-incidents/', deleted_incidents, name='deleted_incidents'),
]
