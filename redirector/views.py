from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import UrlShrinked
from .forms import UrlShrinkedForm
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.sites.shortcuts import get_current_site
from django.http import JsonResponse,HttpResponse
from hashids import Hashids
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import requests

#View used on site, make shrinked code from post request passed by form or inflate form in the html view
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

#View redirect me to the right url
def url_redirection(request, code):
    url_retrieved=get_url(code)
    if(url_retrieved!=None):
        return redirect(url_retrieved.url)
    else:
        return render(request,'redirector/error.html')

#Get url from shrinked code (Json)
#Csrf is disabled for get post request from external site without cookie or sessions
@csrf_exempt
def api_url_response(request,code):
    result=get_url(code)
    if(result!= None):
        object_response={'url':result.url,'shrink':result.shrinked_code}
        response=HttpResponse(JsonResponse(object_response), content_type="application/json")
    else:
        response=HttpResponse(JsonResponse({'url':'null'}), content_type="application/json")
    return response

#Get shrinked code from url (Json)
#Csrf is disabled for get post request from external site without cookie or sessions
@csrf_exempt
def api_url_request(request):
    if request.method=="POST":
        url_verification=URLValidator()
        post_url=request.POST.get('url');
        result=UrlShrinked(url="")
        if post_url:
            try:
                url_verification(post_url)
                result.url=post_url
                result.save()
                result.publish()
            except Exception as e:
                result.url="url_invalid"
                result.shrinked_code="url_invalid"
        else:
            result.url="url_empty"
            result.shrinked_code="url_empty"
    object_response={'url':result.url,'shrink':result.shrinked_code}
    return HttpResponse(JsonResponse(object_response), content_type="application/json")

#Search url using shrinked code, private function, TO MOVE
def get_url(code):
    try:
        return UrlShrinked.objects.get(shrinked_code=code)
    except UrlShrinked.DoesNotExist:
        return None


