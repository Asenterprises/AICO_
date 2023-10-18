```python
from django.shortcuts import render
from .models import QualityCheck
from .forms import QualityCheckForm
from django.contrib.auth.decorators import login_required

@login_required
def quality_home(request):
    checks = QualityCheck.objects.all()
    return render(request, 'quality/index.html', {'checks': checks})

@login_required
def quality_check(request):
    if request.method == 'POST':
        form = QualityCheckForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_home')
    else:
        form = QualityCheckForm()
    return render(request, 'quality/check_form.html', {'form': form})
```