from django.db import models

# Create your models here.

class Tasks(models.Model):
    PURPOSE = (
         ('Personal','Personal'),
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
    title = models.CharField(max_length=50)
    place = models.CharField(max_length=16, choices=PLACE, default='City Proper')
    note = models.TextField(max_length=100, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
         ordering = ('-date_created',)
    
    def __str__(self):
        return self.title