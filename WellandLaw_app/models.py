from django.db import models
import uuid
from ckeditor.fields import RichTextField 

class BoardMember(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/images/boardmembers', default = 'static/images/boardmembers/default.jpg')

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
    title = models.CharField(max_length=200)
    links = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Members(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    firm = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10, blank=True, null=True)
    fax =  models.CharField(max_length=10, blank=True, null=True)
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

    def __init__(self):
        return self.title


class Job(models.Model):
    date = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=200)
    organization = models.CharField(max_length=300, blank=True, null=True)
    link = models.URLField(max_length=2000, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.organization
