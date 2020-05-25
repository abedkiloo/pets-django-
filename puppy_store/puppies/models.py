from django.db import models


# Create your models here.
class Puppies(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    breed = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    created_at = models.DateField(auto_now=True)
    update_at = models.DateField(auto_now=True)

    def get_breed(self):
        return self.name + " belongs to " + self.breed + " breed."

    def __repr__(self):
        return self.name + ' is added.'
