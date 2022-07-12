from django.forms import ModelForm

from .models import Link


class AddForm(ModelForm):
    class Meta:
        model = Link
        fields = ('author', 'link')