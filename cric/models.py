from django.db import models
from django.contrib.auth.models import User

class Cricket(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # User deletion doesn't delete recipes

    def __str__(self):
        return self.name  # Returns recipe name in Django admin
    

# class Team(models.Model):
#     team = models.CharField(max_length=100)
    

#     def __str__(self) -> str:
#         return self.team

#     class Meta:
#         ordering = ['team']


# class Type(models.Model):
#     type = models.CharField(max_length=100)

#     def __str__(self) -> str:
#         return self.type


# class Award(models.Model):
#     award = models.CharField(max_length=100)

#     def __str__(self) -> str:
#         return self.award
    

# class Tropies(models.Model):
#     tropie = models.CharField(max_length=100)

#     def __str__(self)->str:
#         return self.tropie

    

# class Player(models.Model):
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     award = models.ForeignKey(Award, on_delete=models.CASCADE)
#     Tropies = models.ForeignKey(Tropies, on_delete=models.CASCADE)
#     Player_name = models.CharField(max_length=100)
#     Player_birthdate = models.CharField(max_length=100, unique=True)
#     player_age = models.IntegerField(default=18)
#     player_spouse = models.CharField(default='single')
#     no_odi = models.IntegerField(default=0)
#     odi_score = models.IntegerField(default=0)
#     no_test = models.IntegerField(default=0)
#     test_score = models.IntegerField(default=0)
#     no_t20 = models.IntegerField(dafault=0)
#     t20_score = models.IntegerField(default=0)
#     player_address = models.TextField()

#     def __str__(self) -> str:
#         return self.student_name

#     class Meta:
#         ordering = ['player_name']
#         verbose_name = "Player"


