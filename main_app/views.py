import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Card, Merch, Photo
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
    id_list = card.merchen.all().values_list('id')
    merchen_card_doesnt_have = Merch.objects.exclude(id__in=id_list)
    apraisal_form = ApraisalForm()
    return render(request, 'cards/detail.html', { 
        'card': card, 'apraisal_form': apraisal_form,
        'merchen': merchen_card_doesnt_have
        })

class CardCreate(CreateView):
    model = Card
    fields = ['number', 'anime', 'description', 'year']

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
  
  
class MerchList(ListView):
    model = Merch
    
class MerchDetail(DetailView):
    model = Merch
    
class MerchCreate(CreateView):
    model = Merch
    fields = '__all__'
    
class  MerchUpdate(UpdateView):
    model = Merch
    fields = ['name', 'item']
    
class MerchDelete(DeleteView):
    model = Merch
    success_url = '/merchen'
    
def assoc_merch(request, card_id, merch_id):
    Card.objects.get(id=card_id).merchen.add(merch_id)
    return  redirect('detail', card_id=card_id)
    
def unassoc_merch(request, card_id, merch_id):
    Card.objects.get(id=card_id).merchen.remove(merch_id)
    return redirect('detail', card_id=card_id)


def add_photo(request, card_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, card_id=card_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', card_id=card_id)