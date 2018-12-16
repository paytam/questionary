from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Geneder(models.Model):
    genderCode=models.IntegerField(primary_key=True)
    genderDescription=models.TextField(null=True)

class Country(models.Model):
    countryCode = models.IntegerField(primary_key=True)
    countryName= models.TextField(null=False)

class State(models.Model):
    countryCode = models.ForeignKey(Country, on_delete=models.CASCADE)
    stateName= models.TextField(null=False)

class City(models.Model):
    stateCode = models.ForeignKey(State, on_delete=models.CASCADE)
    cityName= models.TextField(null=False)

class Address(models.Model):
    city =models.OneToOneField(City, on_delete=models.CASCADE)
    number=models.TextField(null=True)
    zipCode=models.TextField(null=True)
    street=models.TextField(null=True)

class Passport(models.Model):
    passportNumber=models.IntegerField;
    passportExpiryDate=models.DateField;
    country=models.ForeignKey(Country, on_delete=models.CASCADE)

class Citizen(models.Model):
    countryId=models.ForeignKey(Country, on_delete=models.CASCADE)
    citizenFromDate=models.DateField(null=True)
    citizenToDate=models.DateField(null=True)
    passport=models.ForeignKey(Passport, on_delete=models.CASCADE)

class MaritalStatusType(models.Model):
    maritalStatusType= models.IntegerField(primary_key=True)
    maritalStatusTypeDescription = models.TextField(null=True)


class Person(models.Model):
    firstName=models.TextField(max_length=100)
    lastName=models.TextField(max_length=100)
    middleName=models.TextField(max_length=100)
    dateOfBirth=models.DateField()
    dateOfDeath=models.DateField(null=False)
    gender=models.OneToOneField(Geneder, on_delete=models.CASCADE)
    # livingAddress=models.ForeignKey(Address, on_delete=models.CASCADE,related_name='Person.livingAddress')
    # birthAddress=models.ForeignKey(Address, on_delete=models.CASCADE,related_name='Person.birthAddress')

class Identification(models.Model):
    country=models.ForeignKey(Country, on_delete=models.CASCADE)
    IdentificationNumber=models.BigIntegerField()
    IdentificationNumberFromDate=models.DateField(null=True)
    IdentificationNumberToDate =models.DateField(null=True)

class MaritalStatus(models.Model):
    maritalStatusType=models.OneToOneField(MaritalStatusType, on_delete=models.CASCADE)
    maritalStatusFromDate=models.DateField
    maritalStatusToDate=models.DateField(null=True)
    maritalStatus=models.ForeignKey(Person, on_delete=models.CASCADE)
