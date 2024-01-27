from django.shortcuts import render
from .models import News
# Create your views here.
def HomeView(request):
    latest_new=News.published.order_by('-id').first()
    news=News.published.order_by('-id')[:5]
    context={
        "latest_new":latest_new,
        "news":news,
    }
    return render(request,'index.html',context)
