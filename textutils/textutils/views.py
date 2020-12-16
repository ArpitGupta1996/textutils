# I have created this file
from django.http import HttpResponse
from django.shortcuts import render  #this is for the template folder we made

def index(request):
    #return HttpResponse("Home")
    return render(request,'index.html')

def analyze(request):
    #Get the text
    djtext=request.POST.get('text', 'default')   #through the GET function whatever we type under our text utils website that will come under url because of GET function. so instead of GET we will use POST
    #Check the checkbox value
    removepunc=request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    extraspaceremover=request.POST.get('extraspaceremover', 'off')
    #Check with checkbox is on
    if removepunc=="on":
        # analyzed=djtext
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        #analayze the text
        #return render(request,'analyze.html',params)
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {'purpose': 'Change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # analayze the text
        #return render(request, 'analyze.html', params)

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # analayze the text
        #return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Remove NewLines', 'analyzed_text': analyzed}
        #djtext = analyzed
        # analayze the text
        #return render(request, 'analyze.html', params)
    if(removepunc !="on" and newlineremover !="on" and fullcaps !="on" and extraspaceremover !="on"):
        return HttpResponse("Please select any operations")

    return render(request, 'analyze.html', params)

# def capfirst(request):
#     return HttpResponse("captalize first")
#
# def newlineremove(request):
#     return HttpResponse("new line remover")
#
# def spaceremove(request):
#     return HttpResponse("space remover <a href='/'>back</a>")
#
# def charcount(request):
#     return HttpResponse("charcount")