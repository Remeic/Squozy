from django.shortcuts import render
from django.utils import timezone
from .models import UrlShrinked
from .forms import UrlShrinkedForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.sites.shortcuts import get_current_site
from django.http import JsonResponse,HttpResponse
from hashids import Hashids
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import requests

# Create your views here.

def create_shorturl(request):
    if request.method == "POST":
        form=UrlShrinkedForm(request.POST)
        if form.is_valid():
            url=form.save(commit=False)
            url.save()
            url.publish()
            tmp="/"+url.shrinked_code+"/"
            full_url = ''.join(['http://', get_current_site(request).domain,tmp])
            return render(request, 'redirector/shrink_detail.html', {'url_skrink': full_url})
    else:
        form=UrlShrinkedForm()
    return render(request, 'redirector/create.html',{'form':form})


def url_redirection(request, code):
    url_retrieved=get_url(code)
    if(url_retrieved!=None):
        return redirect(url_retrieved.url)
    else:
        return render(request,'redirector/error.html')

def api_url_response(request,code):
    result=get_url(code)
    if(result!= None):
        object_response={'url':result.url,'shrink':result.shrinked_code}
        response=HttpResponse(JsonResponse(object_response), content_type="application/json")
    else:
        response=HttpResponse(JsonResponse({'url':'null'}), content_type="application/json")
    return response

#Doesn't work, url can't dispatch this view
def api_url_request(request,aurl):
    result=UrlShrinked()
    val = URLValidator(verify_exists=True)
    try:
        val=(aurl)
        result(url=aurl)
        result.save()
        result.publish()
    except Exception as e:
        result(url=null,shrinked_code=null)
    object_response={'url':result.url,'shrink':result.shrinked_code}
    return HttpResponse(JsonResponse(object_response), content_type="application/json")


def get_url(code):
    try:
        return UrlShrinked.objects.get(shrinked_code=code)
    except UrlShrinked.DoesNotExist:
        return None


