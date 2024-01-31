# basic
# from django.http import HttpResponse
# from django.shortcuts import render
# def index(request):
#     return  render(request,'index.html')

# def about(request):
#     return  HttpResponse("hello aditya")
# def removepuc(request):
#     print(request.GET.get('text','default'))
#     return  HttpResponse("remove punch")


from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return  render(request,'index.html')

def about(request):
    return  HttpResponse("hello aditya")

def ex1(request):
    sites = ['''<h1>For Entertainment  </h1> <a href="https://www.youtube.com/"> Youtube Videos</a> ''',
             '''<h1>For Interaction  </h1> <a href="https://www.facebook.com/"> Facebook</a> ''',
             '''<h1>For Insight  </h1> <a href="https://www.ted.com/talks"> Ted Talks</a> ''',
             '''<h1>For Internship  </h1> <a href="https://www.internshala.com">Internship</a> ''']
    return HttpResponse((sites))







def analyser(request):
     #Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext=analyzed            
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if fullcaps=="on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext=analyzed
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if extraspaceremover=="on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        djtext=analyzed
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        djtext=analyzed
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        # return render(request, 'analyze.html', params)
    # else:
    #     return HttpResponse("Error")  
    return render(request, 'analyze.html', params)
