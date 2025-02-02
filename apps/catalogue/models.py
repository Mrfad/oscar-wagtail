from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractCategory, AbstractProduct

class Product(AbstractProduct):
    COLOR_CHOICES = [
         ('green', 'Green'),
         ('white', 'White'),
         ('blue', 'Blue'),
         ('black', 'Black'),
         ('purple', 'Purple'),
         ('pink', 'Pink'),
         ('orange', 'Ornge'),
         ('yellow', 'Yellow'),
         ('red', 'Red'),
         ('grey', 'Grey'),
         ('brown', 'Brown'),
         ('silver', 'Silver'),
         ('gold', 'Gold'),
    ]

    color = models.CharField(max_length=50, choices=COLOR_CHOICES, default="white")

class Category(AbstractCategory):
    def get_cat_num_products(cat, count=0):
        if cat.has_children():
            for c in cat.get_children():
                count += c.get_cat_num_products()
        else:       
            return ProductCategory.objects.filter(category=cat).count()
        
        count += ProductCategory.objects.filter(category=cat).count()

        return count

    def get_num_products(self):
            return self.get_cat_num_products()


from oscar.apps.catalogue.models import * 