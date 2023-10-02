from django import forms
from .models import Gym


class GymForm(forms.ModelForm):

    class Meta:
        model = Gym
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
