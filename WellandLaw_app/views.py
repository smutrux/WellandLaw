from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    events = Event.objects.order_by('date').all()
    context = {'events': events}
    return render(request, 'index.html', context)


def aboutus(request):
    board = BoardMember.objects.all()
    context = {'board': board}
    return render(request, 'about-us.html', context)


def careercentre(request):
    roles = Role.objects.all()
    jobs = Job.objects.order_by('date').all()

    if request.method == 'POST':
        # Retrieving the form's information
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        adName = request.POST['adName']
        adCategory = request.POST['adCategory']
        document = request.FILES['document']
        # initialize the variables for email and backend

        subject = "Ad slot request: " + name
        message = "Phone #: " + phone + "\n" + "Email: " + email + "\n" + "Title of Ad: " + adName + "\n" + "Category: " + adCategory + "\n"
        # got rid of file as it would throw an error that could not be fixed easily

        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        messages.add_message(request, messages.SUCCESS,
                             'Your inquiry has been submitted successfully. We will get back to you shortly.')

        update = CareerCentre(name=name, email=email, phone=phone, adName=adName, adCategory=adCategory, document=document)
        update.save()
        print("data uploaded to db")

        return redirect('career-centre')

    context = {'roles': roles, 'jobs': jobs}
    return render(request, 'career-centre.html', context)


def contactus(request):
    if request.method == 'POST':
        # Retrieving the form's information
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        firm = request.POST['firm']
        subject = request.POST['subject']
        message = request.POST['message']

        # initialize the variables for email and backend

        subject = "Contact: " + name + " - " + subject
        message = "Phone #: " + phone + "\n" + "Email: " + email + "\n" + "Firm: " + firm + "\n" + message

        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        messages.add_message(request, messages.SUCCESS,
                             'Your inquiry has been submitted successfully. We will get back to you shortly.')

        update = ContactUs(name=name, email=email, phone=phone, firm=firm, subject=subject, message=message)
        update.save()
        print("data uploaded to db")
        return redirect('contact-us')

    return render(request, 'contact-us.html')


def cpdevents(request):
    events = Event.objects.order_by('date').all()
    context = {'events': events}
    return render(request, 'cpd-events.html', context)


def eventsdetails(request, pk):
    event = Event.objects.get(id=pk)
    context = {'event': event}
    return render(request, 'events-details.html', context)


def landingpage(request):
    return render(request, 'landing-page.html')


def membershippage(request):
    members = Members.objects.all()

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

        messages.add_message(request, messages.SUCCESS,
                             'Your inquiry has been submitted successfully. We will get back to you shortly.')

        return redirect('membership-page')

    context = {'members': members}
    return render(request, 'membership-page.html', context)


def practiceportals(request):
    sections = PracticePortal.objects.all()
    context = {'sections': sections}
    return render(request, 'practice-portals.html', context)


def pdf_viewer(request):
    pdf = get_obejt_or


def library(request):
    sections = Library.objects.all()
    context = {'sections': sections}
    return render(request, 'library.html', context)


def publicresources(request):
    resources = PublicResources.objects.all()
    context = {'resources': resources}
    return render(request, 'public-resources.html', context)
