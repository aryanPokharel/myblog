from django.shortcuts import render
from .models import Article


# Create your views here.

def articles_view(request):
    articles = Article.objects.all()

    word = "Hey There"
    context = {
        'word': word,
        'articles' : articles
    }
    return render(request, 'articles.html', context)
