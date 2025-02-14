from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publisher = models.CharField(max_length=100)
    release_date = models.DateField()
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'books'