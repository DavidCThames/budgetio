from django.http import HttpResponse
from django.shortcuts import render
from .models import Expences
from collections import Counter

# Create your views here.
def search(request):
    if request.method=='GET' and request.GET.get('search-housing') is not None:
        data = request.GET

        new_data = Expences.objects.get(salary=data['search-new-salary'])
        pref_data = {
            "food":             int(data['search-food']),
            "housing":          int(data['search-housing']),
            "transportation":   int(data['search-transportation']),        
            "healthcare":       int(data['search-healthcare']),    
            "taxes":            int(data['search-taxes']),
            "other":            int(data['search-other'])
        }
        pref_data['savings'] = int(data['search-old-salary']) - (12 * (pref_data['food'] + pref_data['housing'] + pref_data['transportation'] + pref_data['healthcare'] + pref_data['taxes'] + pref_data['other']))

        # budget = {
        #     "housing": int(data['search-housing']),
        #     "utilities": int(data['search-utilities']),
        #     "food": int(data['search-food']),
        #     "other": int(data['search-other'])
        # }
        # budget['savings'] = int(data['search-new-salary']) - (12 * (budget['housing'] + budget['utilities'] + budget['food'] + budget['other']))

        budget = {
            "food":             new_data.food,
            "housing":          new_data.housing,
            "transportation":   new_data.transportation,        
            "healthcare":       new_data.healthcare,    
            "taxes":            new_data.taxes,
            "other":            new_data.other
        }
        budget['savings'] = new_data.salary - (new_data.food + new_data.housing + new_data.transportation + new_data.healthcare + new_data.taxes + new_data.other)

        budget = shift_for_pref(budget, pref_data)
    

        return render(request, 'budget_calc/results.html',  {'budget': budget})

    return render(request, 'budget_calc/search.html')


def shift_for_pref(data_avg, data_pref):
    # Get the total salary of each dataset
    data_avg_total = sum(data_avg.values(), 0.0)
    data_pref_total = sum(data_pref.values(), 0.0)

    # Convert data_pref to the same total as data_avg
    for key in data_pref:
        data_pref[key] = int(data_pref[key] * data_avg_total / data_pref_total)

    data_sum = dict(Counter(data_avg) + Counter(data_pref))

    for key in data_sum:
        data_sum[key] = int(data_sum[key] / 2)
    return data_sum