```python
from django.shortcuts import render
from .models import Warehouse
from .forms import WarehouseForm
from django.contrib.auth.decorators import login_required

@login_required
def warehouse_list(request):
    warehouses = Warehouse.objects.all()
    return render(request, 'warehouse/index.html', {'warehouses': warehouses})

@login_required
def warehouse_detail(request, pk):
    warehouse = Warehouse.objects.get(id=pk)
    return render(request, 'warehouse/detail.html', {'warehouse': warehouse})

@login_required
def warehouse_new(request):
    if request.method == "POST":
        form = WarehouseForm(request.POST)
        if form.is_valid():
            warehouse = form.save(commit=False)
            warehouse.save()
            return redirect('warehouse_detail', pk=warehouse.pk)
    else:
        form = WarehouseForm()
    return render(request, 'warehouse/new.html', {'form': form})

@login_required
def warehouse_edit(request, pk):
    warehouse = Warehouse.objects.get(id=pk)
    if request.method == "POST":
        form = WarehouseForm(request.POST, instance=warehouse)
        if form.is_valid():
            warehouse = form.save(commit=False)
            warehouse.save()
            return redirect('warehouse_detail', pk=warehouse.pk)
    else:
        form = WarehouseForm(instance=warehouse)
    return render(request, 'warehouse/edit.html', {'form': form})
```