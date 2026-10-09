from django.contrib import admin
from emergency.models import EmergencyRequest,RiskPrediction

# Register your models here.
admin.site.register(EmergencyRequest)
admin.site.register(RiskPrediction)
