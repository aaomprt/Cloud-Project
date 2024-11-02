from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class AnimalType(models.Model):
    name = models.CharField(max_length=50, unique=True)  # e.g., "Dog", "Cat"

    def __str__(self):
        return self.name


class Breed(models.Model):
    animal_type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100) # e.g., "Siamese", "Golden Retriever"

    class Meta:
        unique_together = ('animal_type', 'name') # Ensure unique breed within each animal type


    def __str__(self):
        return f"{self.animal_type} - {self.name}"



class Owner(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # Link to Django's User model for authentication (optional)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.TextField(blank=True)  # Allow blank address
    email = models.EmailField(blank=True) # Allow blank email, if user is registered

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Pet(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    animal_type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True, blank=True)  # Allow null and blank breed
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)  # Allow blank birthdate
    sex = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True) # More inclusive options
    medical_history = models.TextField(blank=True) # Allow blank medical history


    def __str__(self):
        return self.name


class Appointment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason = models.TextField()  # Description of the appointment reason
    notes = models.TextField(blank=True) # Notes taken during/after the appointment


    def __str__(self):
        return f"{self.pet.name} - {self.date}"



class MedicalRecord(models.Model):  # Replaces Treatment model to be more general
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True, blank=True) # Link to Appointment, but allow records outside scheduled appointments (e.g., emergency)
    date = models.DateTimeField() 
    # การวินิจฉัย
    diagnosis = models.TextField(blank=True)  
    # การรักษา
    treatment = models.TextField(blank=True)  
    # medication
    medication = models.TextField(blank=True) # Add field for medication given


    def __str__(self):
        return f"{self.pet.name} - {self.date}"