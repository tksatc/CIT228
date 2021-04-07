from django.db import models


# Create your models here.
class Pizza(models.Model):
    """A model of a type of pizza"""
    name = models.CharField(max_length=100)

    def __str__(self):
        """Return a string representation of a pizza"""
        return self.name


class Topping(models.Model):
    """A model of a pizza topping"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "toppings"

    def __str__(self):
        """Return a string representation of the model"""
        return f"{self.name}"
