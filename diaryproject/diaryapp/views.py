from django.shortcuts import render, redirect
from .forms import EntryForm
from .models import Entry

# Create your views here.
def index(request):
    entries = Entry.objects.order_by('-date_posted')
    return render(request, 'diaryapp/index.html', {'entries':entries})

def add(request):

    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    form = EntryForm()
    
    return render(request, 'diaryapp/add.html', {'form':form})