from django.db import models
from django.contrib.auth.models import User
from django_quill.fields import QuillField
import uuid

def get_image_filepath(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return f'post_images/{instance.title}/{filename}'

def get_CV_filepath(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return f'CV/{instance.job}/{filename}'

def get_Cover_letter_filepath(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return f'CV/{instance.job}/{filename}'

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = QuillField()
    image = models.ImageField(upload_to=get_image_filepath, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=50)  # Par exemple, plein temps, partiel, freelance
    posted_at = models.DateTimeField(auto_now_add=True)
    last_date_to_apply = models.DateField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-posted_at']

class Applicant(models.Model):
    email = models.TextField(default='bdiouipierre@gmail.com')
    first_name = models.CharField(max_length=100, default="non renseigné")
    last_name = models.CharField(max_length=100, default="non renseigné")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applicants')
    phone = models.TextField(default="non renseigné")
    cv = models.FileField(upload_to=get_CV_filepath, null=True, blank=True)
    cover_letter = models.FileField(upload_to=get_Cover_letter_filepath, null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job}"

class Message(models.Model):
    email = models.TextField()
    content = models.TextField()
    first_name = models.CharField(max_length=100, default="non renseigné")
    last_name = models.CharField(max_length=100, default="non renseigné")
    phone = models.TextField(default="non renseigné")
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email + ' : ' + self.submitted_at

class ContactRequest(models.Model):
    # Définir les champs selon le formulaire
    email = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    content = models.TextField()
    phone = models.TextField(default="non renseigné")
    callback_request = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.company}"