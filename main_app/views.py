from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Card
from .forms import ApraisalForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cards_index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', {
        'cards': cards
    })
    
def cards_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    apraisal_form = ApraisalForm()
    return render(request, 'cards/detail.html', { 
        'card': card, 'apraisal_form': apraisal_form 
        })

class CardCreate(CreateView):
    model = Card
    fields = '__all__'

class CardUpdate(UpdateView):
  model = Card
  # Let's disallow the renaming of a card by excluding the name field!
  fields = ['number', 'anime', 'description', 'year']

class CardDelete(DeleteView):
  model = Card
  success_url = '/cards'
  
def add_apraisal(request, card_id):
      # create a ModelForm instance using the data in request.POST
      form = ApraisalForm(request.POST)
      # validate the form
      if form.is_valid():
          # don't save the form to the db until it ha the car_id assigned
          new_apraisal = form.save(commit=False)
          new_apraisal.card_id = card_id
          new_apraisal.save()
      return redirect('detail', card_id=card_id)