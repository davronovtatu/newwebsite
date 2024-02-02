from django.shortcuts import render,get_object_or_404
from .models import News
# Create your views here.
def HomeView(request):
    latest_new=News.published.order_by('-id').first()
    news=News.published.order_by('-id')[:5]
    sport_news=News.published.filter(category__name="Sport")
    texno_news=News.published.filter(category__name="Texnologiya")
    mahalliy_news=News.published.filter(category__name="Mahalliy")
    xorij_news=News.published.filter(category__name="Xorij")


    context={
        "latest_new":latest_new,
        "news":news,
        "sport_news":sport_news,
        "texno_news":texno_news,
        "mahalliy_news":mahalliy_news,
        "xorij_news":xorij_news,
    }
    return render(request,'index.html',context)


def DetailNew(request,slug):
    news=get_object_or_404(News,slug=slug)
    context={
        "news":news
    }
    return render(request,"single-page.html",context)





def SportView(request):
    sport_news=News.published.filter(category__name="Sport")
    context={
        "sport_news":sport_news
    }
    return render(request,"sportnews.html",context)
