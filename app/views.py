from django.shortcuts import render
from django.http import HttpResponse

def near_hundred(request,n):
  return HttpResponse((abs(100 - int(n)) <= 10) or (abs(200 - int(n)) <= 10))


def string_splosion(request,str):
  result = ""
  for i in range(len(str)):
    result = result + str[:i+1]
  return HttpResponse(result)


def cat_dog(request,str):
    return HttpResponse(str.count('cat') == str.count('dog'))


def lone_sum(request,a, b, c):
    values=[int(a),int(b),int(c)]
    counts = {x:values.count(x)for x in values}
    return HttpResponse(sum(x for x in values if counts[x]==1))
        