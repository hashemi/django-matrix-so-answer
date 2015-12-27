from django.shortcuts import render
from .models import *

def index(request):
  all_selections = Selection.objects.all()
  all_people = set([selection.person for selection in all_selections])
  blank_person_counts = {person: 0 for person in all_people}
  all_categories = set([selection.item.category for selection in all_selections])

  categories = []

  for category in all_categories:
    selections = [s for s in all_selections if s.item.category == category]

    total_by_person = blank_person_counts.copy()

    unique_item_details = set([s.item for s in selections])

    items = [{'detail': item_details} for item_details in unique_item_details]
    total_by_item = {item['detail']: 0 for item in items}
    total_by_item_person = {item['detail']: blank_person_counts.copy() for item in items}

    for selection in selections:
      total_by_item_person[selection.item][selection.person] = selection.quantity
      total_by_item[selection.item] += selection.quantity
      total_by_person[selection.person] += selection.quantity

    for item in items:
      item['people_totals'] = [total_by_item_person[item['detail']][person] for person in all_people]
      item['total'] = total_by_item[item['detail']]

    people_totals = [total_by_person[person] for person in all_people]
    category_total = sum(people_totals)

    categories.append({
      'detail': category.name,
      'people_totals': people_totals,
      'total': category_total,
      'items': items
    })

  context = {'people': all_people, 'categories': categories}
  return render(request, 'matrix.html', context)
