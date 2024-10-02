from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.template import loader


class IndexView(generic.TemplateView):
    template_name = 'identity/mypanel/index.html'

class SecondPageView(generic.TemplateView):  # Neue View für die zweite Seite
    template_name = 'mypanel/second_page.html'

def testing(request):
    template = loader.get_template('mypanel/index.html')
    context = {
        'firstname': 'Linus',
    }
    return HttpResponse(template.render(context, request))

