from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404
from .models import Store
from .form import ChaiForm

# Create your views here.
def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'chai/all_chai.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'chai/chai_detail.html', {'chai': chai})

def chai_store(request):
    stores = None
    if request.method == 'POST':
        form = ChaiForm(request.POST)
        if form.is_valid():
            chai = form.cleaned_data['chai_varity']
            stores = Store.objects.filter(chai_variety=chai)
    else:
        form = ChaiForm()
        stores = Store.objects.all()
    return render(request, 'chai/chai_store.html', {'form': form, 'stores': stores})