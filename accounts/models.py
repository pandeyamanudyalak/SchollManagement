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
