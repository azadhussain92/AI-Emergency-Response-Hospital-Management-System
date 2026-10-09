from django.contrib import admin
from hospital.models import Hospital,Department,Bed

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Department)
admin.site.register(Bed)
