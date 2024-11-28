from django.shortcuts import render, redirect

from .forms import advertiserListForm
from .models import advertiserList
# Create your views here.

def advertiser_list(request):
    applies = advertiserList.objects.filter(completed=False)
    return render(request, 'list.html', {'applies':applies})

def advertiser_list_post(request):
    if request.method == "POST":
        form = advertiserListForm(request.POST)
        if form.is_valid():
            apply = form.save(commit=False)
            apply.save()
            return redirect('advertiser_list')
        else:
            form=advertiserListForm()
        return render(request, 'createList.html',{'form',form})