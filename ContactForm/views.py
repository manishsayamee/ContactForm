from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import TemplateView


from rest_framework.generics import CreateAPIView,ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from .models import ContactModel
from .serializer import ContactModelSerializer


class ContactModelCreateAPI(CreateAPIView):
  serializer_class = ContactModelSerializer
  
  def perform_create(self, serializer):
    serializer.save()
    print("Serializer is save")
    

class ContactModelListAPI(ListAPIView):
  serializer_class = ContactModelSerializer
  queryset = ContactModel.objects.all()


class ContactModelDestoryAPI(DestroyAPIView):
  # serializer_class = ContactModelSerializer
  queryset = ContactModel.objects.all()

class ContactModelUpdateAPI(UpdateAPIView):
  serializer_class = ContactModelSerializer
  queryset = ContactModel.objects.all()

class ContactModeRetriveAPI(RetrieveAPIView):
  serializer_class = ContactModelSerializer
  queryset = ContactModel.objects.all()

