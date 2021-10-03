from django.db import models

# Create your models here.

PLATE_TYPE=(
    ('c', 'curved'),
    ('f', 'flat'),
    ('a', 'aluminum'),
    ('w', 'wooden')
)

class Plates(models.Model):
    name= models.CharField(max_length=50)
    description= models.TextField()
    price= models.FloatField()
    plate_images= models.ImageField(upload_to='plateimg')
    category= models.CharField(choices=PLATE_TYPE, max_length=20)

    def __str__(self):
        return str(self.id)

