from django import forms

from .models import Item

class StockForm(forms.ModelForm):


  class Meta:
    model = Item
    fields = ('name', 'category', 'quantity', 'price','note',)