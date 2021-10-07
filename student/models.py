from django.db import models


class Student(models.Model):
    first_name = models.CharField(
        max_length=12,null=True
    )
    last_name = models.CharField(
        max_length=12,null=True
    )
    age = models.PositiveSmallIntegerField(null=True)
    date_of_birth = models.DateField(null=True)
    national_id= models.CharField(
        max_length= 20,null=True
    )
    profile = models.ImageField(upload_to ='images/',null=True)
    nationality_choice=(
        ('1','Rwandan'),
        ('2','Kenyan'),
        ('3','Ugandan'),
        ('4','South Sudanese'),
        ('5','Sudanese')
    )

    nationality = models.CharField(
        max_length=15, choices=nationality_choice,null=True
    )
    gender_choice=(
        ('1','Female'),
        ('2','male'),
        ('3','none')
    )
    gender = models.CharField(
        max_length=8, choices=gender_choice,null=True
    )
    guardian_name = models.CharField(
        max_length=12,null=True
    )
    email_address= models.EmailField(null=True)
    district = models.CharField(
        max_length=12,null=True
    )
    phone_number = models.CharField(
        max_length=12,
        null=True
    )
    medical_report = models.FileField(upload_to='documents/',null=True)
    date_of_enrollment = models.DateField(null=True)


    course_name = models.CharField(
        max_length=18,
        null=True
    )
    languages_choice=(
        ('1','English'),
        ('2','Kinyarwanda'),
        ('3','French'),
        ('4','Kiswahili'),
        ('5','Luganda')

    )

    languages = models.CharField(
        max_length=20, choices=languages_choice,null=True
    )
    laptop_number = models.CharField(
        max_length=10,blank=True,null=True
    )
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def year_of_birth(self):
        return 2021-self-age

# Create your models here.
