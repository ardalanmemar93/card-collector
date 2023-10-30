from django.shortcuts import render


cards = [
    {'name': "Tetsuo's Dream", 'from': "Akira", 'description': "Tetsuo dreams about being in a lab and getting tested on.", 'year': 1987},
    {'name': "Kiyoko's Dream", 'from': "Akira", 'description': "She dreams about tetsuo destroying the city", 'year': 1987},
    {'name': "Neo Tokyo", 'from': "Akira", 'description': "Neo Tokyo was built by 2019, the city pulses with light, sound, motion and apparentprosperity.", 'year': 1987},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cards_index(request):
    return render(request, 'cards/index.html', {
        'cards': cards
    })