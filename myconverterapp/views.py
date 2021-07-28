from django.shortcuts import render
from django.http import HttpResponse
from django import forms

def home(request):
    return HttpResponse("Welcome to My Converter App")

def myconverterapp(request):
    return render(request,'index.html')

# To Submit query & show result
def submitquery(request):
    q = request.POST['query']
    try:
        ans = eval(q)
        mydictionary = {
            "q" : q,
            "ans" : ans,
            "error" : False,
            "result" : True
        }
        return render(request,'index.html',context=mydictionary)

    except:
        mydictionary = {
            "error": True,
            "result" : False
        }
        return render(request, 'index.html', context=mydictionary)

# To Feedback
class SimpleForm(forms.Form):
    firstname = forms.CharField(max_length=400)
    q = firstname

def feedback(request):
    form = SimpleForm(request.POST)
    mydiction = {
        "form": form
    }
    return render(request,'index.html', context=mydiction)