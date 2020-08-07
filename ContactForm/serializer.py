from rest_framework import serializers
from .models import ContactModel



class ContactModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = ContactModel
    fields = ['id','first_name', 'last_name', 'address', 'number', 'email']
    read_only_fields = ['id']

