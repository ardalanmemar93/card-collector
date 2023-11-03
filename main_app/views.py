import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Card, Merch, Photo
from .forms import ApraisalForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def cards_index(request):
    cards = Card.objects.filter(user=request.user)
    return render(request, 'cards/index.html', {
        'cards': cards
    })


@login_required   
def cards_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    id_list = card.merchen.all().values_list('id')
    merchen_card_doesnt_have = Merch.objects.exclude(id__in=id_list)
    apraisal_form = ApraisalForm()
    return render(request, 'cards/detail.html', { 
        'card': card, 'apraisal_form': apraisal_form,
        'merchen': merchen_card_doesnt_have
        })

class CardCreate(LoginRequiredMixin, CreateView):
    model = Card
    fields = ['number', 'anime', 'description', 'year']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CardUpdate(LoginRequiredMixin, UpdateView):
  model = Card
  # Let's disallow the renaming of a card by excluding the name field!
  fields = ['number', 'anime', 'description', 'year']

class CardDelete(LoginRequiredMixin, DeleteView):
  model = Card
  success_url = '/cards'


@login_required  
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
  
  
class MerchList(LoginRequiredMixin, ListView):
    model = Merch
    
class MerchDetail(LoginRequiredMixin, DetailView):
    model = Merch
    
class MerchCreate(LoginRequiredMixin, CreateView):
    model = Merch
    fields = '__all__'
    
class  MerchUpdate(LoginRequiredMixin, UpdateView):
    model = Merch
    fields = ['name', 'item']
    
class MerchDelete(LoginRequiredMixin, DeleteView):
    model = Merch
    success_url = '/merchen'


@login_required   
def assoc_merch(request, card_id, merch_id):
    Card.objects.get(id=card_id).merchen.add(merch_id)
    return  redirect('detail', card_id=card_id)


@login_required    
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


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)