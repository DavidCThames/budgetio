from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def search(request):
    if request.method=='GET':
        data = request.GET
        budget = {
            "housing": int(data['search-housing']),
            "utilities": int(data['search-utilities']),
            "food": int(data['search-food']),
            "other": int(data['search-other'])
        }
        budget['savings'] = int(data['search-new-salary']) - (12 * (budget['housing'] + budget['utilities'] + budget['food'] + budget['other']))

        return render(request, 'budget_calc/results.html',  {'budget': budget})

    return render(request, 'budget_calc/search.html')