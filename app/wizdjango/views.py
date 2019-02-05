from django.shortcuts import render
from .forms import FormStepOne, FormStepTwo
from formtools.wizard.views import SessionWizardView

# Create your views here.
def index(request):
    return render(request, 'wizdjango/index.html', {})

class FormWizardView(SessionWizardView):
    template_name = 'wizdjango/multiform.html'
    form_list = [FormStepOne, FormStepTwo]

    def done(self, form_list, form_dict, **kwargs):
        return render(self.request, 'wizdjango/done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })
