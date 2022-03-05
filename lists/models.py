from datetime import datetime
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Tasks(models.Model):
     PURPOSE = (
          ('Personal','Personal'),
          ('Fitness','Fitness'),
          ('School', 'School'),
          ('Business','Business'),        
          ('Office','Office'),        
     )

     PLACE = (
          ('City Proper', 'City Proper'),
          ('Jaro', 'Jaro'),
          ('La Paz', 'La Paz'),
          ('Lapuz', 'Lapuz'),
          ('Mandurriao', 'Mandurriao'),
          ('Molo', 'Molo'),
          ('Villa Arevalo', 'Villa Arevalo'),
          ('Lapuz', 'Lapuz'),
     )
          
     purpose = models.CharField(max_length=8, choices=PURPOSE, default='Personal')
     title = models.CharField(max_length=50, unique=True)
     completed = models.BooleanField(default=False)
     slug = models.SlugField(max_length=50, unique=True, blank=True)
     place = models.CharField(max_length=16, choices=PLACE, default='City Proper')
     note = models.TextField(max_length=100, blank=True)
     date_created = models.DateTimeField(default=datetime.now, blank=True)

     # class Meta:
     #      ordering = ['-date_created']

     def save(self, *args, **kwargs):
         self.slug = slugify(self.title)
         super(Tasks, self).save(*args, **kwargs)   
     
     def __str__(self):
        return self.title
   