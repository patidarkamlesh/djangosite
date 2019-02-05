from django.urls import path
from . import views

from wizdjango.forms import FormStepOne, FormStepTwo
from wizdjango.views import FormWizardView
app_name = 'wizdjango'

urlpatterns = [
    #path('', views.index, name="index"),
   path('', FormWizardView.as_view([FormStepOne, FormStepTwo])),
]
