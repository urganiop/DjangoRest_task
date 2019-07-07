from django.db import models


class Order(models.Model):
    description = models.TextField(verbose_name= 'описание' , blank= True )
    price = models.DecimalField(verbose_name= 'цена' , max_digits= 8 , decimal_places= 0 , default= 0 )