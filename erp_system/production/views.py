```python
from django.shortcuts import render
from .models import Production
from .forms import ProductionForm
from django.contrib.auth.decorators import login_required

@login_required
def production_list(request):
    productions = Production.objects.all()
    return render(request, 'production/index.html', {'productions': productions})

@login_required
def production_detail(request, id):
    production = Production.objects.get(id=id)
    return render(request, 'production/detail.html', {'production': production})

@login_required
def production_new(request):
    if request.method == "POST":
        form = ProductionForm(request.POST)
        if form.is_valid():
            production = form.save(commit=False)
            production.save()
            return redirect('production_detail', id=production.id)
    else:
        form = ProductionForm()
    return render(request, 'production/new.html', {'form': form})

@login_required
def production_edit(request, id):
    production = Production.objects.get(id=id)
    if request.method == "POST":
        form = ProductionForm(request.POST, instance=production)
        if form.is_valid():
            production = form.save()
            return redirect('production_detail', id=production.id)
    else:
        form = ProductionForm(instance=production)
    return render(request, 'production/edit.html', {'form': form})
```