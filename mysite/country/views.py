from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Country

# Create your views here.
def index(request):
    return HttpResponse("hello country")


def all_countries(request):
    countries = Country.objects.all()
    #     return render(request, 'bears/bear_list.html', {'bears': bears})

    return render(request, 'all_countries.html', {'countries': countries})
