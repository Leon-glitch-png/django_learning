from django.db import models

# Create your models here.

GENRES_TYPES = [
    ('action', 'Action'),
    ('adventure', 'Adventure'),
    ('casual','Casual'),
    ('simulation', 'Simulation'),
    ('strategy', 'Strategy'),
    ('sports', 'Sports'),
    ('rpg', 'RPG'),
    ('racing', 'Racing'),
    ('software', 'Software'),
    ('shooter', 'Shooter'),
    ('survival', 'Survival'),
    ('multiplayer', 'Multiplayer'),
]

class Genres(models.Model):
    name = models.CharField(max_length=12, choices=GENRES_TYPES)
   
    def __str__(self):
        return self.name
    


class Games(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ManyToManyField(Genres, related_name='games',blank=True)
    release_date = models.DateField()
    icon = models.ImageField(upload_to='game_icons/')
    
    def __str__(self):
        return self.name
    



class Detail(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Email: {self.email}, Address: {self.address}'