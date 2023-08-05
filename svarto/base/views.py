from django.shortcuts import render
from .models import (
    AboutUs,
    TeamMember,
    WhatWeDoItem,
    NewsItem,
)
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def index(request):
    about = AboutUs.objects.first()
    team_members = TeamMember.objects.all()
    what_we_do_items = WhatWeDoItem.objects.all()
    news_items = NewsItem.objects.all()
    form = ContactForm()

    return render(
        request,
        "base.html",
        {
            "request": request,
            "about": about,
            "team_members": team_members,
            "what_we_do_items": what_we_do_items,
            "news_items": news_items,
            "form": form,
        },
    )


def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["txtName"]
            email = form.cleaned_data["txtEmail"]
            phone = form.cleaned_data["txtPhone"]
            message = form.cleaned_data["txtMsg"]
            subject = f"New Contact Form Submission from {name}"
            body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
            sender_email = settings.EMAIL_HOST_USER
            recipient_list = [
                "general@svarto.am",
            ]
            send_mail(subject, body, sender_email, recipient_list)
            return render(request, "success.html")
        else:
            return render(request, "not_success.html")
    else:
        form = ContactForm()
        return render(request, "not_success.html")
