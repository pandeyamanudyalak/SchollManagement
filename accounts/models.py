from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from accounts.managers import CustomUserManager



class CustomUser(AbstractBaseUser, PermissionsMixin):
    FINICIAL_YEAR = [
        ('23-24','2023-2024')
    ]
    college_name = models.CharField(max_length=200,null=True,blank=True)
    college_id = models.IntegerField(
        unique=True,
        validators=[MinValueValidator(limit_value=100000, message="College ID must be at least 6 digits."), MaxValueValidator(limit_value=999999, message="College ID must be at most 6 digits.")]
        )
    user_id = models.IntegerField(
        unique=True,
        validators=[MinValueValidator(limit_value=100000, message="User ID must be at least 6 digits."), MaxValueValidator(limit_value=999999, message="College ID must be at most 6 digits.")]
    )
    financial_year = models.CharField(choices=FINICIAL_YEAR,max_length=5)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'college_id'
    REQUIRED_FIELDS = ['user_id', 'financial_year']

    def __str__(self):
        return str(self.college_id)
    


class College(models.Model):
    college_id = models.CharField(max_length=6, unique=True)
    name = models.CharField(max_length=255)
    motto = models.CharField(max_length=255, blank=True, null=True)
    established = models.PositiveIntegerField()
    location_city = models.CharField(max_length=255)
    location_state = models.CharField(max_length=255)
    location_country = models.CharField(max_length=255, choices=[('IN', 'INDIA')])
    accreditation = models.TextField(null=True, blank=True)
    college_type = models.CharField(max_length=20, choices=[('public', 'Public'), ('private', 'Private')])
    website = models.URLField(null=True, blank=True)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    about = models.TextField(null=True, blank=True)
    college_logo = models.ImageField(upload_to='images')
    college_banner = models.ImageField(upload_to='images')
    
    president_name = models.CharField(max_length=255, null=True, blank=True)
    president_bio = models.TextField(null=True, blank=True)

    library = models.BooleanField(default=False)
    dormitories = models.BooleanField(default=False)
    sports_facilities = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.college_id:
            self.generate_unique_college_id()
        super(College, self).save(*args, **kwargs)

    def generate_unique_college_id(self):
        from random import randint
        while True:
            college_id = ''.join([str(randint(0, 9)) for _ in range(6)])
            if not College.objects.filter(college_id=college_id).exists():
                self.college_id = college_id
                break

    def __str__(self):
        return self.name  
