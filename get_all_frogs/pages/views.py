from django.shortcuts import render
from get_all_frogs.models import Zabka, VisitedZabkas

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            token = request.POST.get('token')
            try:
                zabka = Zabka.objects.get(token=token)
                print(zabka.token + zabka.localization)
                visited, c = VisitedZabkas.objects.get_or_create(visitor=request.user)
                visited.zabka.add(zabka)
                return render(request, 'pages/valid.html')
            except:
                return render(request, 'pages/invalid.html')
    return render(request, 'pages/home.html')


def visited_zabkas(request):
    if request.user.is_authenticated:
        visited_list = VisitedZabkas.objects.filter(visitor=request.user)
        return render(request, 'pages/visited.html', {'visited_list': visited_list})
    return render(request, 'pages/home.html')    