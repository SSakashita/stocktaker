from django.shortcuts import render
from django.utils import timezone

from .models import Item


def item_list(request):
  items = Item.objects.filter(stocked_date__lte=timezone.now()).order_by('stocked_date')
  return render(request, 'stocktaker/item_list.html', {'items': items})