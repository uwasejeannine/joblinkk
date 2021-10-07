from django.db import models

class Trainer(models.Model):
    first_name= models.CharField(
        max_length=12
    )
    last_name = models.CharField(
        max_length=12
    )
    age = models.PositiveSmallIntegerField()
    gender_choice=(
        ('1','Female'),
        ('2','male'),
        ('3','none')
    )
    gender = models.CharField(
        max_length=8, choices=gender_choice, null=True
    )
    bio= models.TextField(
        max_length=700, null=True
    )
    email_address= models.EmailField(null=True)
    phone_number = models.CharField(
        max_length=12, null=True
    )
    salary= models.PositiveBigIntegerField(null=True)
    nationality_choice=(
        ('1','Rwandan'),
        ('2','Kenyan'),
        ('3','Ugandan'),
        ('4','South Sudanese'),
        ('5','Sudanese')
    )

    nationality = models.CharField(
        max_length=15, choices=nationality_choice,null=True)
    profile= models.ImageField(upload_to ='images/', null=True)
    contract= models.FileField(upload_to='documents/', null=True)
    date_hired= models.DateField(null=True)
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

# Create your models here.
