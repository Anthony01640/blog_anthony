from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404

from appli.forms import Mail
from .models import Articles


# Create your views here.


def home(request):
    return render (request, "appli/home.html")


def affiche_article(request):
    liste_articles = Articles.objects.all
    return render (request, "appli/blog.html", {"articles": liste_articles})


def article_description(request, name):
    article = get_object_or_404 (Articles, name=name)
    return render (request, "appli/article.html", {"article": article})


def contact(request):
    if request.method == 'GET':
        form = Mail()
        return render(request, "appli/me.html", {"form" : form})
    elif request.method == 'POST':
        form = Mail(request.POST)
        if form.is_valid():
            send_mail(
                'form.subject',
                'form.message',
                'form.mail',
                ['Anthony.dubuis@outlook.fr'],
                fail_silently=False,
            )
            return render(request, "appli/blog.html")
        else:
            return render(request, "appli/home.html")



def cv(request):
    return render(request, 'appli/cv.html')
