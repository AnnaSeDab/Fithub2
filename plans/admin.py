from django.contrib import admin
from .models import DayPlan, PlanCategory, FitnessPlan


admin.site.register(DayPlan)
admin.site.register(PlanCategory)
admin.site.register(FitnessPlan)