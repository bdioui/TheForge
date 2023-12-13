from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, JobForm
from .models import *
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.conf import settings
from django.contrib import messages
import os

# Create your views here.
def Index(request):
    posts = Post.objects.all()
    return render(request, 'Main/Index.html', {'posts':posts})

def AI(request):
    return render(request, 'Main/AI.html')

def Cyber(request):
    return render(request, 'Main/Cyber.html')

def IoT(request):
    return render(request, 'Main/IoT.html')

def About(request):
    return render(request, 'Main/About.html')

def Join(request):
    jobs = Job.objects.all()
    return render(request, 'Main/Join.html', {"jobs":jobs})

def Blog(request):
    posts = Post.objects.all()
    return render(request, 'Main/Blog.html', {"posts":posts})

def Contact(request):
    if request.method == "POST":
        message = Message(
            email=request.POST.get('email'),
            content=request.POST.get('content')
        )
        message.save()
        sender_email = request.POST.get('email')
        content = request.POST.get('content')
        email_template = get_template(os.path.join(settings.BASE_DIR, 'Main/templates/Main/message_confirmation.html'))

        subject = 'Message reçu !'
        email_body = email_template.render()
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [sender_email]

        email = EmailMessage(subject, email_body, from_email, recipient_list)
        email.content_subtype = 'html'
        email.send()

        # Préparation de l'email pour l'administrateur avec les pièces jointes
        admin_email = EmailMessage(
            f'Nouveau message de {sender_email}',
            f'message : {content}',
            settings.EMAIL_HOST_USER,
            ['bdiouipierre@gmail.com']  # Remplacez par l'email de l'administrateur
        )

        admin_email.send()
        messages.success(request, 'Votre message a bien été envoyé !')
        return redirect('Main:index')
    else:
        return render(request, 'Main/Contact.html')

def Post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {"post":post}
    return render(request, 'Main/Post.html', context)

def Create_Post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Ajoutez request.FILES pour traiter les fichiers

        if form.is_valid():
            # L'instance 'post' est créée et sauvegardée en une seule étape
            post = form.save(commit=False)
            post.author = request.user  # Assurez-vous d'assigner l'auteur si le champ est obligatoire
            post.save()

            # Redirigez vers la page de confirmation ou de détail de l'article
            return redirect('Main:post', pk=post.pk)

    else:
        form = PostForm()

    return render(request, 'Main/Create_Post.html', {'form': form})

def Job_Detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    jobs = Job.objects.all()
    context = {"job": job, 'jobs': jobs}

    if request.method == "POST":
        application = Applicant(
            email=request.POST.get('email'),
            job=job,
            cv = request.FILES.get('cv'),
            cover_letter = request.FILES.get('cover_letter'),
            )
        application.save()

        context = {'job_title': job.title}  # Remplacez par les données réelles
        email = request.POST.get('email')
        email_template = get_template(os.path.join(settings.BASE_DIR, 'Main/templates/Main/job_confirmation.html'))

        subject = 'Message reçu !'
        email_body = email_template.render(context)
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        email = EmailMessage(subject, email_body, from_email, recipient_list)
        email.content_subtype = 'html'
        email.send()

        # Préparation de l'email pour l'administrateur avec les pièces jointes
        admin_email = EmailMessage(
            f'Nouvelle candidature pour {job.title}',
            f'Une nouvelle candidature a été soumise pour le poste : {job.title}.',
            settings.EMAIL_HOST_USER,
            ['bdiouipierre@gmail.com']  # Remplacez par l'email de l'administrateur
        )

        cv_file = request.FILES.get('cv')
        cover_letter_file = request.FILES.get('cover_letter')

        if cv_file:
            admin_email.attach(cv_file.name, cv_file.read(), cv_file.content_type)
        if cover_letter_file:
            admin_email.attach(cover_letter_file.name, cover_letter_file.read(), cover_letter_file.content_type)

        admin_email.send()
        messages.success(request, 'Votre candidature a bien été envoyée !')
        return redirect('Main:join')
    else :
        return render(request, 'Main/Job.html', context)

def Create_Job(request):
    if request.method == 'POST':
        print('POSTED')
        # Création d'un nouvel objet Job directement avec les données du POST
        job = Job(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            location=request.POST.get('location'),
            type=request.POST.get('type'),  # Assurez-vous que 'job_type' est le nom correct du champ dans votre modèle
            last_date_to_apply=request.POST.get('last_date_to_apply')
        )
        # Vous pouvez ajouter ici des champs supplémentaires si nécessaire
        job.save()  # Sauvegardez l'objet dans la base de données
        messages.success(request, "Nouvel offre d'emploi créée !")
        return redirect('Main:job', pk=job.pk)
    else:
        return render(request, 'Main/Create_Job.html')


