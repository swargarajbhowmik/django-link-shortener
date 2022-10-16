from textwrap import shorten
from django.shortcuts import render, redirect
from .models import *
import random
import string

# Create your views here.
def IndexPage(request):
    return render(request, 'app/index.html')

def ShortenURL(request):
    URL = request.POST['url']
    shortedLink = ''.join(random.choices(string.ascii_lowercase, k=6))    
    Shorten = LinksList.objects.create(URL=URL,ShortedLink=shortedLink)
    ShortenedURL = "http://localhost:8000/go/"+shortedLink

    if 'usr_data' in request.session:
        updateDic = request.session['usr_data']

        print(URL)
        print(updateDic)

        if URL in updateDic.keys():
            del updateDic[URL]
            updateDic[URL]=ShortenedURL
            request.session['usr_data'] = updateDic
        else:
            updateDic[URL]=ShortenedURL
            request.session['usr_data'] = updateDic

    else:
        request.session['usr_data'] = {}
        updateDic = request.session['usr_data']
        updateDic[URL]=ShortenedURL
        request.session['usr_data'] = updateDic

    # shortendURLS
    return redirect("http://localhost:8000/#link-shortner-section")

def GoPageRedirect(request, sht_url):
    try:
        getLinkData = LinksList.objects.get(ShortedLink=sht_url)
        return redirect(getLinkData.URL)
    except:
        return redirect('http://localhost:8000/404')