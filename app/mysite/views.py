from django.shortcuts import render
from .models import contact
import requests, json

# Create your views here.
def index(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name  = request.POST.get('lname')
    else:
        first_name = 'Kamlesh'
        last_name  = 'Patidar'
    joke = getJoke(first_name, last_name)
    return render(request, 'mysite/index.html', {'joker' : joke})

def mycontact(request):
    if request.method == 'POST':
        contact_email = request.POST.get('contact_email')
        contact_subject = request.POST.get('contact_subject')
        contact_message = request.POST.get('contact_message')
        c = contact(email = contact_email, subject = contact_subject, message = contact_message)
        c.save()
        return render(request, 'mysite/thanks.html', {})
    else:
        return render(request, 'mysite/contact.html', {})

def portfolio(request):
    return render(request, 'mysite/portfolio.html', {})

def getJoke(fname, lname):
    jokeurl = 'http://api.icndb.com/jokes/random?firstName='+fname+'&amp;lastName='+lname
    req = requests.get(jokeurl)
    json_data = json.loads(req.text)
    joke = (json_data.get('value').get('joke')).replace('Norris', lname)
    return joke

