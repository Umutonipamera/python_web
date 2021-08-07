from django.db import models
import datetime
from django.core.validators import MaxValueValidator,MinValueValidator
#import phone number

from django.db import models

# Create your models here.

def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

NATIONALITY=(
    ("Kenyan","Kenyan"),
    ("Ugandan","Ugandan"),
    ("Rwandan","Rwandan"),
    ("South Sudanese","South Sudanese"),
)
GENDER=(
    ("Male","Male"),
    ("Female","Female"),
    ("Non-Binary","Non-Binary"),
    ("Transgender","Transgender"),

)

# Create your models here.



class Trainer (models.Model):
       first_name=models.CharField(max_length=12)
       last_name=models.CharField(max_length=20)
       nationlity=models.CharField(max_length=20,choices= NATIONALITY, default='Kenyan')
       gender=models.CharField(max_length=12,choices=GENDER, default='Male')
       id=models.CharField(primary_key=True,max_length=20)
       email=models.EmailField(null=True)
       phoneNumber=models.CharField(max_length=16,null=True)
       course=models.CharField(max_length=20)
       contract=models.FileField(upload_to='documents/%y/%m/%d',null=True)
       Resume=models.FileField(upload_to='documents/%y/%m/%d',null=True)
       Salary=models.PositiveBigIntegerField()
       Company=models.CharField(max_length=20)
       profile_picture=models.ImageField(upload_to="images|",null=True)
       