from quarterback.irs.models import *
from django.shortcuts import render_to_response, HttpResponse


def index(request):
    
    if request.GET and request.GET['q'] and len(request.GET['q'])>2:
        q = request.GET['q']
        #results = Nonprofit.objects.filter(name__icontains=q).order_by('name','-year')
        results = Nonprofit.objects.extra(where=['body_tsv @@ plainto_tsquery(%s)'], params=[q])
    else:
        q = ''
        results = [] #Nonprofit.objects.all().order_by('-assetts')[:50]
       
           
    return render_to_response('nonprofits.html', {'results': results, 'q': q })

