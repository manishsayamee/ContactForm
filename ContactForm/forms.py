from .models import ContactModel
from django.forms import ModelForm




class ContactForm(ModelForm):
  class Meta:
    model = ContactModel
    fields = ['first_name', 'last_name', 'email', 'address', 'number']
