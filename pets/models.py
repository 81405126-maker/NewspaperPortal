from django.db import models

class Pet(models.Model):
    PET_TYPE_CHOICES = [
        ("dog", "Dog"),
        ("cat", "Cat"),
        ("bird", "Bird"),
        ("hamster", "Hamster"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=50)
    pet_type = models.CharField(max_length=10, choices=PET_TYPE_CHOICES)
    special_talent = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="pets/", blank=True, null=True)
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.pet_type})"
