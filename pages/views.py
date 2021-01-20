from django.shortcuts import render
from django.http import HttpResponse
from fjb.models import Jualan

# Create your views here.
def index(request):
    fjb = Jualan.objects.order_by('tanggal').filter(is_published=True)[:3]

    context = {
        'fjb' : fjb
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
