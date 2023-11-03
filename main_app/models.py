from django.db import models
from django.urls import reverse
from datetime import date

GRADES = [
    ('P', 'Pristine'),
    ('B', 'Bad'),
    ('G', 'Good'),
]


# Create your models here
class Merch(models.Model):
    name = models.CharField(max_length=50)
    item = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('merchen_detail', kwargs={'pk': self.id})


class Card(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    anime = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    merchen = models.ManyToManyField(Merch)

    def __str__(self):
        return f'{self.name} ({self.id})'

def get_absolute_url(self):
    return reverse('detail', kwargs={'card_id': self.id})
    
def appraised_for_current_month(self):
    today = date.today()
    return self.apraisal_set.filter(date__month=today.month, date__year=today.year).count() 

class Apraisal(models.Model):
    date = models.DateField('apraisal date')
    grade = models.CharField(
        max_length=1,
        choices=GRADES,
        default=GRADES[2][0],
    )
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_grade_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
        
   
class Photo(models.Model):
    url = models.CharField(max_length=200)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Photo for card_id: {self.card_id} @{self.url}"
    