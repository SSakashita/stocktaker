from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Item

from .forms import StockForm


def item_list(request):
  items = Item.objects.filter(stocked_date__lte=timezone.now()).order_by('stocked_date')
  return render(request, 'stocktaker/item_list.html', {'items': items})

def item_detail(request, pk):
  item = get_object_or_404(Item, pk=pk)
  return render(request, 'stocktaker/item_detail.html', {'item': item})

def item_new(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.stocked_date = timezone.now()
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = StockForm()
    return render(request, 'stocktaker/item_edit.html', {'form': form})

def item_edit(request, pk):
  item = get_object_or_404(Item, pk=pk)
  if request.method == 'POST':
    form = StockForm(request.POST, instance=item)
    if form.is_valid():
      item = form.save(commit=False)
      item.author = request.user
      item.stocked_date = timezone.now()
      item.save()
      return redirect('item_detail', pk=item.pk)
  else:
    form = StockForm(instance=item)
  return render(request, 'stocktaker/item_edit.html', {'form': form})