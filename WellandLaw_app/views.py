from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'about-us.html')

def careercentre(request):
    return render(request, 'career-centre.html')

def contactus(request):
    return render(request, 'contact-us.html')

def cpdevents(request):
    return render(request, 'cpd-events.html')

def eventsdetails(request, pk):
    return render(request, 'events-details.html')

def landingpage(request):
    return render(request, 'landing-page.html')

def library(request):
    return render(request, 'library.html')

def membershippage(request):
    return render(request, 'membership-page.html')

def practiceportals(request):
    return render(request, 'practice-portals.html')

def publicresources(request):
    return render(request, 'public-resources.html')

def test(request):
    return render(request, 'test.html')

