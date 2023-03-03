from django.forms import ModelForm
from .models import Feeding

# Register your models here.
class FeedingForm(ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']