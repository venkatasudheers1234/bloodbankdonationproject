from django.contrib import admin
from . models import donor

from . models import blood
from . models import hospital
from . models import bloodBank
from . models import Employee
from . models import orders



admin.site.register(donor)
admin.site.register(blood)
admin.site.register(bloodBank)
admin.site.register(hospital)
admin.site.register(Employee)
admin.site.register(orders)
# Register your models here.

