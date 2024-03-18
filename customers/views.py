from django.http import HttpResponse
from django.template import loader

def customers(request):
  # Variables in Django, youll pass it like this and parse it as pizzaname in general in html
  var = {'pizzaname': 'Mozzarella'}
  template = loader.get_template('index.html')
  return HttpResponse(template.render(var, request))