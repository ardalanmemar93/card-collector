from django.shortcuts import render


cards = [
    {'name': "Tetsuo's Dream",  'number': 22, 'from': "Akira", 'description': "Tetsuo dreams about being in a lab and getting tested on.", 'year': 1987},
    {'name': "Kiyoko's Dream", 'number': 23,  'from': "Akira", 'description': "She dreams about tetsuo destroying the city", 'year': 1987},
    {'name': "Neo Tokyo", 'number': 2,  'from': "Akira", 'description': "Neo Tokyo was built by 2019, the city pulses with light, sound, motion and apparentprosperity.", 'year': 1987},
     {'name': "Faithful Kaori",  'number': 70, 'from': "Akira", 'description': "Kaori finally reaches the remains of the olympic stadium", 'year': 1987},
      {'name': "The Calm Before",  'number': 69, 'from': "Akira", 'description': "The Colonel watches the debris from SOL rain like shooting stars on Neo Tokyo", 'year': 1987},
       {'name': "Akira Reborn", 'number': 76, 'from': "Akira", 'description': "A small figure appears in the light, translucent for a moment, then solid.", 'year': 1987},
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