from django.shortcuts import render, redirect
from .models import Cycle  # Make sure this line is here

def dashboard(request):
    cycles = Cycle.objects.all().order_by('-id')
    latest = cycles.first() if cycles.exists() else None

    # Calculations
    if latest:
        next_period = latest.last_period_date + timedelta(days=latest.cycle_length)
        ovulation = latest.last_period_date + timedelta(days=latest.cycle_length//2)
        fertile_start = ovulation - timedelta(days=2)
        fertile_end = ovulation + timedelta(days=2)
    else:
        next_period = ovulation = fertile_start = fertile_end = None

    context = {
        'cycles': cycles,
        'latest': latest,
        'next_period': next_period,
        'ovulation': ovulation,
        'fertile_start': fertile_start,
        'fertile_end': fertile_end,
    }
    return render(request, 'dashboard.html', context)

def add_cycle(request):
    if request.method == 'POST':
        last_period_date = request.POST.get('last_period_date')
        cycle_length = int(request.POST.get('cycle_length'))
        Cycle.objects.create(
            last_period_date=last_period_date,
            cycle_length=cycle_length
        )
        return redirect('dashboard')
    return render(request, 'add_cycle.html')

# ✅ Reset feature
def reset_cycles(request):
    if request.method == 'POST':
        Cycle.objects.all().delete()
    return redirect('dashboard')
