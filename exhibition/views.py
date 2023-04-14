from django.shortcuts import render
from django.views import View
from .models import ExhibitionPlace


class ExhibitionPlacesView(View):
  template_name = "exhibition/exhibition-places.html"
  def get(self, request):
    exhibition_places = ExhibitionPlace.objects.all()
    context = {"exhibition_places": exhibition_places}
    return render(request, self.template_name, context)
exhibition_place = ExhibitionPlacesView.as_view()