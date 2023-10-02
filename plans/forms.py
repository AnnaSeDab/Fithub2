from django import forms
from .models import DayPlan, PlanCategory, FitnessPlan


class PlanForm(forms.ModelForm):

    class Meta:
        model = FitnessPlan
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        plancategories = PlanCategory.objects.all()
        dayplan = DayPlan.objects.all()

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class FitnessCategoryForm(forms.ModelForm):

    class Meta:
        model = PlanCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'