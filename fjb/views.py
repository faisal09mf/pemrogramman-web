from django.shortcuts import get_object_or_404, render
from .models import Jualan
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def index(request):
    
    fjb = Jualan.objects.order_by('tanggal').filter(is_published=True)

    paginator = Paginator(fjb, 6)
    page = request.GET.get('page')
    page_fjb = paginator.get_page(page)

    context = {
        'fjb': page_fjb
    }
    
    return render(request, 'fjb/fjb.html', context)

def jualan(request, jualan_id):
  
   item = get_object_or_404(Jualan, pk=jualan_id)

   context = {
       'item': item
   }
   
   return render(request, 'fjb/jualan.html', context)

def search(request):
    return render(request, 'fjb/search.html')