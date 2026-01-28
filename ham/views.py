from django.shortcuts import render
from .models import Ham
from .forms import HamForm, UserRegistrationForm 
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
def index(request):
    return render(request, 'index.html')

def ham_list(request):
    hams = Ham.objects.all().order_by('-created_at')
    return render(request, 'ham_list.html', {'hams': hams})

@login_required
def ham_create(request):
    if request.method == 'POST':
        form = HamForm(request.POST, request.FILES)
        if form.is_valid():
            ham = form.save(commit=False)
            ham.user = request.user
            ham.save()
            return redirect('ham_list')
    else:
        form = HamForm()
    return render(request, 'ham_form.html', {'form': form})


@login_required
def ham_edit(request, user_id):
    ham = get_object_or_404(Ham, pk=user_id, user=request.user)
    if request.method == 'POST':
        form = HamForm(request.POST, request.FILES, instance=ham)
        if form.is_valid():
            form.save()
            return redirect('ham_list')
    else:
        form = HamForm(instance=ham)
    return render(request, 'ham_form.html', {'form': form})
@login_required
def ham_delete(request, user_id):
    ham = get_object_or_404(Ham, pk=user_id, user=request.user)
    if request.method == 'POST':
        ham.delete()
        return redirect('ham_list')
    return render(request, 'ham_confirm_delete.html', {'ham': ham})



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
          user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()
        login(request, user)
        return redirect('ham_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})