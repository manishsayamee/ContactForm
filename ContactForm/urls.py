from django.urls import path
from .views import ContactModelCreateAPI, ContactModelDestoryAPI, ContactModelListAPI,ContactModelUpdateAPI,ContactModeRetriveAPI


app_name ='contact'

urlpatterns=[
  # contact/create/
  path('create/',ContactModelCreateAPI.as_view()),
  path('list/',ContactModelListAPI.as_view()),
  path('update/<int:pk>/',ContactModelUpdateAPI.as_view()),
  path('delete/<int:pk>/',ContactModelDestoryAPI.as_view()),
  path('retrive/<int:pk>/',ContactModeRetriveAPI.as_view()),

]