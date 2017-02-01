from django.shortcuts import render
from django.http import HttpResponse

import dmapp.script as s
import json

from dmapp.models import MovieEntry, ParamEntry
from threading import Thread

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):

  if request.method == 'POST':
    if request.is_ajax():
      print request.POST
      action = request.POST.get('action')

      if action == "get_movies":
        response_data = dealAjax(request)
        return HttpResponse(json.dumps(response_data),content_type='application/json')

      elif action == "run_update":
        response_data = run_update(request)
        return HttpResponse(json.dumps(response_data),content_type='application/json')

      elif action == "check_update":
        response_data = check_update()
        return HttpResponse(json.dumps(response_data),content_type='application/json')

      elif action == "save_changes":
        response_data = save_changes(request)
        return HttpResponse(json.dumps(response_data),content_type='application/json')

  else:
    return render(request, 'index.html', locals())

def run_update(request):
  p = ParamEntry.objects.get(mName='sessionTP')
  p.mValue = request.POST.get('sessionTP')
  p.save()

  s.getMoviesJSON(p.mValue)
  t = Thread(target = s.parseJson())
  t.daemon = True
  t.start()

  p = ParamEntry.objects.get(mName='isUpdating')
  p.mValue = 'true'
  p.save()

  return json.dumps('{\'runing_update\': \''+p.mValue+'\'}')

def check_update():
  p = ParamEntry.objects.get(mName='isUpdating')
  return json.dumps('{\'runing_update\': \''+p.mValue+'\'}')

def save_changes(request):
  m = MovieEntry.objects.get(mID=request.POST.get('idMovie'))
  m.mNew = True if request.POST.get('isNew') == 'true' else False
  m.mSeen = True if request.POST.get('isSeen') == 'true' else False
  m.mWhishlist = True if request.POST.get('isWhishlist') == 'true' else False
  m.save()
  return json.dumps('{\'saving_changes\': \'true\'}')

@csrf_exempt
def dealAjax(request):

  data = request.POST.getlist('filters[]')

  i=0
  n=len(data)
  print data

#  dicti = simplejson.JSONDecoder().decode(data)
#  print dicti

  kwargs = {}
  while i<n:
    if (data[i+1] == 'true' or data[i+1] == 'false'):
      val = True if data[i+1] == 'true' else False
    else:
      val = data[i+1]

    kwargs[data[i]] = val
    i+=2

  print kwargs

  d = MovieEntry.objects.all() 
  finalQ = d.filter(**kwargs)
  dictionaries = [ obj.as_dict() for obj in finalQ ]

  return json.dumps(dictionaries)
