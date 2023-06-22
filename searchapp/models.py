from django.db import models
from django.db.models import JSONField
from django.core.exceptions import ValidationError
import json

def validate_json(value):
    try:
        json.loads(value)
    except json.JSONDecodeError:
        raise ValidationError('Invalid JSON format')


class Dish(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    items = JSONField(null=True,blank=True)
    lat_long = models.CharField(max_length=100)
    full_details =models.TextField(validators=[validate_json])

    def __str__(self):
        return self.name
