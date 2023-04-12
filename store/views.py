from django.shortcuts import render
from django.views import View
from .models import Item

# Create your views here.

class ItemDetails(View):
  template_name = "store/item-details.html"
  def get(self, request, pk):
    item = Item.objects.get(id=pk)
    context = {"item": item}
    return render(request, self.template_name, context)
item_details = ItemDetails.as_view()