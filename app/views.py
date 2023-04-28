from django.shortcuts import render

# Create your views here.
import datetime
def built_in_filters(request):
    
    dt=datetime.datetime.now()
    d={'data':'HAI HOw aRe YoU','dt':dt,'c':0}
    return render(request,'build_in_filters.html',d)
