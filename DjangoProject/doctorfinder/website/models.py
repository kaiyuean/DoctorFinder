from django.db import models
from django.utils import timezone

class Insurance(models.Model):
	INSURANCE_CHOICES = (
		('Aetna', 'Aetna'),
		('Cigna', 'Cigna'),
		('Medicaid', 'Medicaid'),
		('Medicare', 'Medicare'),
		('Tricare', 'Tricare'),
		('Blue', 'Blue'),
		('United', 'United'),
	)
	name = models.CharField(max_length=50, choices=INSURANCE_CHOICES)
	doctor = models.ForeignKey('Doctor',to_field= "username")

class Review(models.Model):
	RATING_CHOICES = (
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5),
	)
	rating = models.IntegerField(choices=RATING_CHOICES)
	comment= models. TextField()
	doctor= models.ForeignKey('Doctor',to_field= "username")
	patient= models.ForeignKey('User',to_field= "username")
	date = models.DateTimeField(default=timezone.now)

class User(models.Model):
	USER_CHOICES = (
		('Admin', 'Admin'),
		('Patient', 'Patient'),
		('Doctor', 'Doctor'),
	)
	name = models.CharField(max_length=30,default='')
	username = models.EmailField(primary_key=True)
	password = models.CharField(max_length=256)
	type= models.CharField(max_length=10, choices=USER_CHOICES)

class Doctor(models.Model):
	SPECIALITY_CHOICES = (
		('Primary Care', 'Primary Care'),
		('Dentist', 'Dentist'),
		('Dermatologist', 'Dermatologist'),
		('ENT', 'ENT'),
		('Eye Doctor', 'Eye Doctor'),
		('Psychiatrist', 'Psychiatrist'),
		('Orthopedist', 'Orthopedist'),
	)
	phoneNumber = models.CharField(max_length =15,default='')
	officeHours = models.CharField(max_length=100,default='')
	speciality = models.CharField(max_length=30, choices=SPECIALITY_CHOICES)
	rating = models.FloatField()
	availability = models.DateField(default='')
	state = models.CharField(max_length=20,default='')
	city = models.CharField(max_length=30,default='')
 	zip = models.CharField(max_length=30,default='')
 	street = models.CharField(max_length=50,default='')
 	education = models.TextField(default='')
	awards = models.TextField(default='')
	experience = models.TextField(default='')
	username = models.OneToOneField('User', to_field= "username",primary_key=True) 
	

class FavoriteDoctors(models.Model):
	patient = models.ForeignKey('User',to_field= "username")
	doctor = models.ForeignKey('Doctor',to_field= "username")
