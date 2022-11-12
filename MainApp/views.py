from django.shortcuts import render
from .forms import facultyMemberForm
from .models import facultyMember

# Create your views here.
def add(request):
    form = facultyMemberForm(request.POST or None)
    #facultyMember = facultyMember.objects.all()
    if form.is_valid():
        form.save()
    return render(request, 'add.html', {'form' : form})
