from django.shortcuts import render
from django.views import View

from .models import *


class IndexView(View):
    template_name = 'courses/index.html'

    def get_context_data(self):
        context = {}
        context['fronts'] = context['fronts'] = Front.objects.order_by('pk').first()
        context['datasets'] = Datasets.objects.all()
        context['statistics'] = Statistics.objects.all()
        context['mentors'] = Mentors.objects.all()
        context['courses'] = Courses.objects.all()
        context['offers_black'] = OffersBlack.objects.all()
        context['offers'] = Offers.objects.all()
        context['gratitudes'] = Gratitude.objects.all()
        context['speakers'] = Speakers.objects.all()
        return context

    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)

def page_not_found_view(request, exception):
    return render(request, 'errors/404.html', status=404)
