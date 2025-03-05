from .models import TeamMember

from django.shortcuts import render, get_object_or_404

from django.shortcuts import render, redirect
from .forms import ContactForm

def index(request):
    team_members = TeamMember.objects.all()
    return render(request, 'main/index.html', {'team_members': team_members})

def about(request): 
    return render(request, 'main/about.html')

def team_member_detail(request, member_id):
    member = get_object_or_404(TeamMember, id=member_id)
    return render(request, 'main/team_member_detail.html', {'member': member})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})