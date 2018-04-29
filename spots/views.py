from django.shortcuts import render

from .models import Spots

# Create your views here.
def index(request):

    spot = Spots.objects.all()

    context = {
        'title': 'by: __Scud__',
        'spots': spot
        }
    return render(request, 'spots/index.html', context)

