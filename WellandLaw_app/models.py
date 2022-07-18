from django.db import models
import uuid

class BoardMember(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    postition = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ExternalLink(models.Model):
    # Add more sections as site develops
    SECTION_CHOICES = (
        ('home', 'Home'),
    )

    display_text = models.CharField(max_length=200)
    url = models.URLField(max_length=2000)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES, blank=True, null=True)


    def __str__(self):
        return self.display_text


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=500)
    image = models.ImageField(upload_to='static/images/event')
    def __str__(self):
        return self.title


class MemberForm(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    firm = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10, blank=True, null=True)
    fax =  models.CharField(max_length=10, blank=True, null=True)
    url = models.URLField(max_length=2000)
    practice = models.CharField(max_length=500)
    number = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class EventForm(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    firm = models.CharField(max_length=300, blank=True, null=True)
    event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class ContactForm(models.Model):
    SUBJECT_CHOICES = (
        ('membership', 'Membership'),
        ('jobs', 'Jobs'),
        ('other', 'Other')
    )

    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    firm = models.CharField(max_length=300, blank=True, null=True)
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES, blank=True, null=True)
    message = models.TextField(max_length=1500)


    def __str__(self):
        return self.name


class Job(models.Model):
    date = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=200)
    organization = models.CharField(max_length=300, blank=True, null=True)
    link = models.URLField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.organization
