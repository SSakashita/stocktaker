from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Item


def item_list(request):
  items = Item.objects.filter(stocked_date__lte=timezone.now()).order_by('stocked_date')
  return render(request, 'stocktaker/item_list.html', {'items': items})

def item_detail(request, pk):
  item = get_object_or_404(Item, pk=pk)
  return render(request, 'stocktaker/item_detail.html', {'item': item})