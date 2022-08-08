from django.shortcuts import render, redirect
from . models import MemberForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

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
    members = MemberForm.objects.all()

    if request.method == 'POST':
        # Retrieving the form's information
        name = request.POST['Name']
        phone = request.POST['Phone-Number']
        email = request.POST['Email']
        company = request.POST['Company']
        areas = ""

        # Check which options were selected
        if 'development' in request.POST:
            areas += 'Business '

        if 'web-design-1' in request.POST:
            areas += 'Civil '

        if 'marketing-1' in request.POST:
            areas += 'Commercial '

        if 'other-1' in request.POST:
            areas += 'Other '      

        # intialize the variables for email and backend

        subject = "Membership Request: " + name 
        message = "Phone #: " + phone + "\n" + "Company: " + company + "\n" + "Email: " + email + "\n" + "Areas of practice: " + areas

        send_mail( 
            subject,
            message,
            email, 
            [settings.EMAIL_HOST_USER], 
            fail_silently=False,
            )

        messages.add_message(request, messages.SUCCESS,'Your inquiry has been submitted successfully. We will get back to you shortly.')

        return redirect('membership-page')

    context = {'members': members}
    return render(request, 'membership-page.html', context)

def practiceportals(request):
    return render(request, 'practice-portals.html')

def publicresources(request):
    return render(request, 'public-resources.html')

def test(request):
    return render(request, 'test.html')

