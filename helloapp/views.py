from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("Xin chao cac ban den voi  hello app cua DJANG ")
    # return render(request,'pages/home_page01.html')
    return render(request, 'pages/login_page01.html')
