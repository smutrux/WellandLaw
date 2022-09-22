from django import forms
from django.db import models
import uuid
from ckeditor.fields import RichTextField


class BoardMember(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/images/boardmembers', default='static/images/boardmembers/default.jpg')

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(blank=True, null=True)
    start = models.TimeField(blank=True, null=True)
    end = models.TimeField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    location = models.CharField(max_length=500)
    image = models.ImageField(upload_to='static/images/event')
    pdf = models.FileField(blank=True, null=True, upload_to="static/documents/event")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class PublicResources(models.Model):
    title = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='static/images/publicresources', blank=True, null=True)
    description = models.CharField(max_length=500)
    links = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "PublicResources"


class Library(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/images/publicresources', blank=True, null=True)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title


class PracticePortal(models.Model):
    FILETYPE_CHOICES = [
        ('pdf', '.pdf'),
        ('hl', 'Link'),
    ]
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=4, choices=FILETYPE_CHOICES, default='hl')
    pdf = models.FileField(blank=True, null=True, upload_to="static/documents/")
    links = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Members(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    firm = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10, blank=True, null=True)
    fax = models.CharField(max_length=10, blank=True, null=True)
    url = models.URLField(max_length=2000)
    practice = models.CharField(max_length=500)
    email = models.EmailField(blank=True, null=True)
    year_called_to_bar = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name_plural = "Members"


class Role(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Job(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    position = models.CharField(max_length=200)
    organization = models.CharField(max_length=300, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    link = models.URLField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.position


class ContactUs(models.Model):
    SUBJECT_CATEGORIES = (
        ('First Choice', 'First Choice'),
        ('Second Choice', 'Second Choice'),
        ('Third Choice', 'Third Choice'),
    )

    name = models.CharField(max_length=300)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    firm = models.CharField(max_length=200)
    subject = models.CharField(max_length=200, default='First Choice', choices=SUBJECT_CATEGORIES)
    message = models.TextField()


class CareerCentre(models.Model):
    AD_CATEGORIES = (
        ('Job Posting', 'Job Posting'),
        ('Student Job Posting', 'Student Job Posting'),
        ('Will Search Notice', 'Will Search Notice'),
        ('Obituary', 'Obituary'),
        ('Legal News', 'Legal News'),
        ('Community Event', 'Community Event'),
        ('Item for Sale or Rent', 'Item for Sale or Rent'),
    )

    name = models.CharField(max_length=300)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    adName = models.CharField(max_length=200)
    adCategory = models.CharField(max_length=200, default='Job Posting', choices=AD_CATEGORIES)
    document = models.FileField(blank=True, null=True, upload_to="static/documents/")
