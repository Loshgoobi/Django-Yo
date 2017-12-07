from django.db import models


class cards(models.Model):
    id = models.IntegerField(max_length=20)
    name = models.CharField(max_length=20)
    level = models.IntegerField(max_length=20)
    attack = models.IntegerField(max_length=20)
    defence = models.IntegerField(max_length=20)
    effect = models.CharField(max_length=500)
    CATEGORY = (
        ('M', 'Monster'),
        ('S', 'Spell'),
        ('T', 'Trap'),
    )
    TYPE = (
        ('Wa', 'Warrior'),
        ('Sp', 'Spellcaster'),
        ('Fa', 'Fairy'),
        ('Fi', 'Fiend'),
        ('Zo', 'Zombie'),
        ('Ma', 'Machine'),
        ('Aq', 'Aqua'),
        ('Py', 'Pyro'),
        ('Ro', 'Rock'),
        ('WB', 'Winged Beast'),
        ('Pl', 'Plant'),
        ('In', 'Insect'),
        ('Th', 'Thunder'),
        ('Dr', 'Dragon'),
        ('Be', 'Beast'),
        ('BW', 'Beast-Warrior'),
        ('Di', 'Dinosaur'),
        ('Fi', 'Fish'),
        ('Se', 'Sea Serpent'),
        ('Ps', 'Psychic'),
        ('DB', 'Divine-Beast'),
        ('CG', 'Creator God'),
        ('Wy', 'Wyrm'),
        ('Cy', 'Cyberse'),


    )
    ATTRIBUTE = (
        ('Ea', 'Earth'),
        ('Wa', 'Water'),
        ('Fi', 'Fire'),
        ('Wi', 'Wind'),
        ('Li', 'Light'),
        ('Da', 'Dark'),
        ('Di', 'Divine'),
    )
# Create your models here.
