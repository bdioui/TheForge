from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, JobForm
from .models import *
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.conf import settings
from django.contrib import messages
import requests
import os

# Create your views here.
def Index(request):
    posts = Post.objects.all().order_by('-created_at')[:6]
    return render(request, 'Main/Index.html', {'posts':posts})
def Charte(request):
    return render(request, 'Main/Charte.html')

def Mentions(request):
    return render(request, 'Main/Mentions.html')

def Conditions(request):
    return render(request, 'Main/Conditions.html')

def FAQ(request):
    if request.method == "POST":
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if result['success']:
            callback_request = request.POST.get('callback_request') == 'on'

            # Mail de confirmation
            email_template = get_template(os.path.join(settings.BASE_DIR, 'Main/templates/Main/request_confirmation.html'))
            email = request.POST.get('email')
            subject = 'Demande reçue !'
            email_body = email_template.render()
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]

            email = EmailMessage(subject, email_body, from_email, recipient_list)
            email.content_subtype = 'html'
            email.send()

            # email pour l'admin du site
            callback_request = request.POST.get('callback_request') == 'on'

            email = request.POST.get('email'),
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            content = request.POST.get('content'),
            company = request.POST.get('company'),
            phone = request.POST.get('phone'),
            field = '-',
            callback_request = 'oui' if callback_request else 'non'

            context = {
                'first_name': request.POST.get('first_name'),
                'last_name': request.POST.get('last_name'),
                'email': request.POST.get('email'),
                'content': request.POST.get('content'),
                'phone': request.POST.get('phone'),
                'field': request.POST.get('field'),
                'company': request.POST.get('company'),
                'callback_request': callback_request,
            }

            # Mail de confirmation
            email_template = get_template(os.path.join(settings.BASE_DIR, 'Main/templates/Main/Admin_alert.html'))
            subject = 'Nouveau message'
            email_body = email_template.render(context)
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['bdiouipierre@gmail.com']

            email = EmailMessage(subject, email_body, from_email, recipient_list)
            email.content_subtype = 'html'
            email.send()
            messages.success(request, 'Votre demande a bien été envoyée !')
            return redirect("Main:faq")
        else:
            messages.error(request, 'Oups ! Erreur de Captcha!')
            return redirect("Main:faq")
    else:
        return render(request, 'Main/FAQ.html')

def AI(request):
    if request.method == "POST":
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if result['success']:
            callback_request = request.POST.get('callback_request') == 'on'
            contact_request = ContactRequest(
                email=request.POST.get('email'),
                first_name = request.POST.get('first_name'),
                last_name = request.POST.get('last_name'),
                content = request.POST.get('content'),
                company = request.POST.get('company'),
                phone=request.POST.get('phone'),
                field = request.POST.get('field'),
                callback_request = callback_request,
            )
            contact_request.save()

            # Mail de confirmation
            email_template = get_template(os.path.join(settings.BASE_DIR, 'Main/templates/Main/request_confirmation.html'))
            email = request.POST.get('email')
            subject = 'Demande reçue !'
            email_body = email_template.render()
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]

            email = EmailMessage(subject, email_body, from_email, recipient_list)
            email.content_subtype = 'html'
            email.send()

            # email pour l'admin du site
            email = request.POST.get('email'),
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            content = request.POST.get('content'),
            company = request.POST.get('company'),
            phone = request.POST.get('phone'),
            field = request.POST.get('field'),
            callback_request = 'oui' if callback_request else 'non'

            context = {
                'first_name': request.POST.get('first_name'),
                'last_name': request.POST.get('last_name'),
                'email': request.POST.get('email'),
                'content': request.POST.get('content'),
                'phone': request.POST.get('phone'),
                'field': request.POST.get('field'),
                'company': request.POST.get('company'),
                'callback_request': callback_request,

            }

            # Mail de confirmation
            email_template = get_template(os.path.join(settings.BASE_DIR, 'Main/templates/Main/Admin_alert.html'))
            subject = 'Nouveau message'
            email_body = email_template.render(context)
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['bdiouipierre@gmail.com']

            email = EmailMessage(subject, email_body, from_email, recipient_list)
            email.content_subtype = 'html'
            email.send()
            messages.success(request, 'Votre demande a bien été envoyée !')
            return redirect('Main:ai')
        else:
            messages.error(request, 'Oups ! Erreur de Captcha!')
            return redirect("Main:ai")
    else:
        return render(request, 'Main/AI.html')

def Cyber(request):
    if request.method == "POST":
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if result['success']:
            callback_request = request.POST.get('callback_request') == 'on'
            contact_request = ContactRequest(
                email=request.POST.get('email'),
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                content=request.POST.get('content'),
                phone=request.POST.get('phone'),
                company=request.POST.get('company'),
                field=request.POST.get('field'),
                callback_request=callback_request,
            )
            contact_request.save()

            # Mail de confirmation
            email_template = get_template(os.path.join(settings.BASE_DIR, 'Main/templates/Main/request_confirmation.html'))
            email = request.POST.get('email')
            subject = 'Demande reçue !'
            email_body = email_template.render()
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]

            email = EmailMessage(subject, email_body, from_email, recipient_list)
            email.content_subtype = 'html'
            email.send()

            # email pour l'admin du site
            email = request.POST.get('email'),
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            content = request.POST.get('content'),
            company = request.POST.get('company'),
            phone = request.POST.get('phone'),
            field = request.POST.get('field'),
            callback_request = 'oui' if callback_request else 'non'

            context = {
                'first_name': request.POST.get('first_name'),
                'last_name': request.POST.get('last_name'),
                'email': request.POST.get('email'),
                'content': request.POST.get('content'),
                'phone': request.POST.get('phone'),
                'field': request.POST.get('field'),
                'company': request.POST.get('company'),
                'callback_request': callback_request,

            }

            # Mail de confirmation
            email_template = get_template(os.path.join(settings.BASE_DIR, 'Main/templates/Main/Admin_alert.html'))
            subject = 'Nouveau message'
            email_body = email_template.render(context)
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['bdiouipierre@gmail.com']

            email = EmailMessage(subject, email_body, from_email, recipient_list)
            email.content_subtype = 'html'
            email.send()
            messages.success(request, 'Votre demande a bien été envoyée !')
            return redirect('Main:cyber')
        else:
            messages.error(request, 'Oups ! Erreur de Captcha !')
    else:
        return render(request, 'Main/Cyber.html')

def IoT(request):
    if request.method == "POST":
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if result['success']:
            callback_request = request.POST.get('callback_request') == 'on'
            contact_request = ContactRequest(
                email=request.POST.get('email'),
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                content=request.POST.get('content'),
                company=request.POST.get('company'),
                phone=request.POST.get('phone'),
                field=request.POST.get('field'),
                callback_request=callback_request,
            )
            contact_request.save()

            # Mail de confirmation
            email_template = get_template(os.path.join(settings.BASE_DIR, 'Main/templates/Main/request_confirmation.html'))
            email = request.POST.get('email')
            subject = 'Demande reçue !'
            email_body = email_template.render()
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]

            email = EmailMessage(subject, email_body, from_email, recipient_list)
            email.content_subtype = 'html'
            email.send()

            callback_request = 'oui' if callback_request else 'non'

            context = {
               'first_name':request.POST.get('first_name'),
               'last_name': request.POST.get('last_name'),
               'email': request.POST.get('email'),
               'content': request.POST.get('content'),
               'phone': request.POST.get('phone'),
               'field': request.POST.get('field'),
               'company': request.POST.get('company'),
               'callback_request': callback_request,

            }

            # Mail de confirmation
            email_template = get_template(os.path.join(settings.BASE_DIR, 'Main/templates/Main/Admin_alert.html'))
            subject = 'Nouveau message'
            email_body = email_template.render(context)
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['bdiouipierre@gmail.com']

            email = EmailMessage(subject, email_body, from_email, recipient_list)
            email.content_subtype = 'html'
            email.send()

            messages.success(request, 'Votre demande a bien été envoyée !')
            return redirect('Main:iot')
        else:
            messages.error(request, 'Oups ! Erreur de Captcha !')
    else:
        return render(request, 'Main/IoT.html')

def About(request):
    if request.method == "POST":
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if result['success']:
            callback_request = request.POST.get('callback_request') == 'on'
            contact_request = ContactRequest(
                email=request.POST.get('email'),
                first_name = request.POST.get('first_name'),
                last_name = request.POST.get('last_name'),
                content = request.POST.get('content'),
                company = request.POST.get('company'),
                field = request.POST.get('field'),
                callback_request = callback_request,
            )
            contact_request.save()

            # Mail de confirmation
            email_template = get_template(os.path.join(settings.BASE_DIR, 'Main/templates/Main/request_confirmation.html'))
            email = request.POST.get('email')
            subject = 'Demande reçue !'
            email_body = email_template.render()
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]

            email = EmailMessage(subject, email_body, from_email, recipient_list)
            email.content_subtype = 'html'
            email.send()

            callback_request = 'oui' if callback_request else 'non'

            context = {
                'first_name': request.POST.get('first_name'),
                'last_name': request.POST.get('last_name'),
                'email': request.POST.get('email'),
                'content': request.POST.get('content'),
                'phone': request.POST.get('phone'),
                'field': request.POST.get('field'),
                'company': request.POST.get('company'),
                'callback_request': callback_request,

            }

            # Mail de confirmation
            email_template = get_template(os.path.join(settings.BASE_DIR, 'Main/templates/Main/Admin_alert.html'))
            subject = 'Nouveau message'
            email_body = email_template.render(context)
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['bdiouipierre@gmail.com']

            email = EmailMessage(subject, email_body, from_email, recipient_list)
            email.content_subtype = 'html'
            email.send()
            messages.success(request, 'Votre demande a bien été envoyée !')
            return redirect('Main:about')
        else:
            messages.error(request, 'Oups ! Erreur de Captcha !')
    else:
        return render(request, 'Main/About.html')

def Join(request):
    jobs = Job.objects.all()
    if request.method == "POST":
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if result['success']:
            application = Applicant(
                email=request.POST.get('email'),
                job=Job.objects.get(title='candidature_libre'),
                cv = request.FILES.get('cv'),
                cover_letter = request.FILES.get('cover_letter'),
                )
            application.save()

            email = request.POST.get('email')
            email_template = get_template(os.path.join(settings.BASE_DIR, 'Main/templates/Main/job_confirmation.html'))

            subject = 'Message reçu !'
            email_body = email_template.render()
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]

            email = EmailMessage(subject, email_body, from_email, recipient_list)
            email.content_subtype = 'html'
            email.send()

            context = {
                'first_name': request.POST.get('first_name'),
                'last_name': request.POST.get('last_name'),
                'email': request.POST.get('email'),
                'phone': request.POST.get('phone'),
            }

            # Récupération des fichiers
            cv_file = request.FILES.get('cv')
            cover_letter_file = request.FILES.get('cover_letter')

            # Chargement du template d'email et génération du contenu
            email_template = get_template(os.path.join(settings.BASE_DIR, 'Main/templates/Main/Admin_applicant.html'))
            email_body = email_template.render(context)

            # Création de l'email
            subject = 'Nouveau message'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['bdiouipierre@gmail.com']
            email = EmailMessage(subject, email_body, from_email, recipient_list)
            email.content_subtype = 'html'

            # Ajout des pièces jointes
            if cv_file:
                email.attach(cv_file.name, cv_file.read(), cv_file.content_type)
            if cover_letter_file:
                email.attach(cover_letter_file.name, cover_letter_file.read(), cover_letter_file.content_type)

            # Envoi de l'email
            email.send()
            messages.success(request, 'Votre candidature a bien été envoyée !')
            return redirect('Main:join')
        else:
            messages.error(request, 'Oups ! Erreur de Captcha !')
    else :
        return render(request, 'Main/Join.html', {'jobs':jobs})


def Blog(request):
    posts = Post.objects.all()
    return render(request, 'Main/Blog.html', {"posts":posts})

def Contact(request):
    if request.method == "POST":
        if request.method == "POST":
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.RECAPTCHA_PRIVATE_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()

            if result['success']:
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


                context = {
                    'first_name': request.POST.get('first_name'),
                    'last_name': request.POST.get('last_name'),
                    'email': request.POST.get('email'),
                    'content': request.POST.get('content'),
                    'phone': request.POST.get('phone'),

                }

                # Mail de confirmation
                email_template = get_template(os.path.join(settings.BASE_DIR, 'Main/templates/Main/Admin_contact.html'))
                subject = 'Nouveau message'
                email_body = email_template.render(context)
                from_email = settings.EMAIL_HOST_USER
                recipient_list = ['bdiouipierre@gmail.com']

                email = EmailMessage(subject, email_body, from_email, recipient_list)
                email.content_subtype = 'html'
                email.send()

                messages.success(request, 'Votre message a bien été envoyé !')
                return redirect('Main:index')
            else:
                messages.error(request, 'Oups ! Erreur de Captcha !')
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
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            phone=request.POST.get('phone'),
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

        context = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
        }

        # Récupération des fichiers
        cv_file = request.FILES.get('cv')
        cover_letter_file = request.FILES.get('cover_letter')

        # Chargement du template d'email et génération du contenu
        email_template = get_template(os.path.join(settings.BASE_DIR, 'Main/templates/Main/Admin_applicant.html'))
        email_body = email_template.render(context)

        # Création de l'email
        subject = 'Nouveau message'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['bdiouipierre@gmail.com']
        email = EmailMessage(subject, email_body, from_email, recipient_list)
        email.content_subtype = 'html'

        # Ajout des pièces jointes
        if cv_file:
            email.attach(cv_file.name, cv_file.read(), cv_file.content_type)
        if cover_letter_file:
            email.attach(cover_letter_file.name, cover_letter_file.read(), cover_letter_file.content_type)

        # Envoi de l'email
        email.send()
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


