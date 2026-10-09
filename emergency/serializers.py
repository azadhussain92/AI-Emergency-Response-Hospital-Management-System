from rest_framework import serializers
from emergency.models import EmergencyRequest

class EmergencyRequestSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.user.username',read_only=True)
    emergency_type_display= serializers.CharField(source='get_emergency_type_display',read_only=True)
    status_display = serializers.CharField(source='get_status_display',read_only=True)

    class Meta:
        model = EmergencyRequest
        fields = [
            'id',
            'patient',
            'patient_name',
            'emergency_type',
            'emergency_type_display',
            'symptoms',
            'heart_rate',
            'oxygen_level',
            'temperature',
            'blood_pressure',
            'location',
            'hospital',
            'doctor',
            'status',
            'status_display',
            'created_at'
        ]

        read_only_fields = [
            'patient',
            'hospital',
            'doctor',
            'status',
            'created_at'
        ]