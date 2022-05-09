from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class Category(models.Model):
    name = models.CharField(_("Category Name"), max_length=255)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(_("Titre"), max_length=255)
    author = models.CharField(_("Auteur"), max_length=255)
    category = models.ForeignKey(Category, verbose_name=_("Nom de la catégorie"), on_delete=models.CASCADE)
    release_date = models.DateField(_("Date de parution"))
    number_of_pages = models.PositiveIntegerField(_("Nombres de pages"))
    resume = models.TextField(_("Resumer "))

    def __str__(self):
        return self.title
    

    