from django.db import models

# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=255 , null=True , blank=True)
    no_of_guests = models.SmallIntegerField()
    BookingDate = models.DateTimeField()

class Menu(models.Model):
    title = models.CharField(max_length=255 , null=True , blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    inventory = models.SmallIntegerField()
    def get_item(self):
       return f'{self.title} : {str(self.price)}'