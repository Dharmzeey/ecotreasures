from django.shortcuts import render
from django.views import View
from store.models import Item, Category

class HomeView(View):
  template_name = "home/index.html"
  def get(self, request):
    items = Item.objects.all()
    categories = Category.objects.all()
    recycled = Item.objects.filter(state=1)
    upcycled = Item.objects.filter(state=2)
    context = {"items": items, "categories": categories, "recycled": recycled, "upcycled": upcycled}
    return render(request, self.template_name, context)
home = HomeView.as_view()


class CategoryFilter(View):
  template_name = "home/index.html"
  def get(self, request, category):
    categories = Category.objects.all()
    filtered_items = Item.objects.filter(category__name=category)
    context = {"filtered_items": filtered_items, "categories": categories, "category": category}
    return render(request, self.template_name, context)
category_filter = CategoryFilter.as_view()
