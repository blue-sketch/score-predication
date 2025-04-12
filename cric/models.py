from django.db import models
from django.contrib.auth.models import User


class Cricket(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username if self.user else "Anonymous User"


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    feed = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Team(models.Model):
    team_image = models.ImageField(upload_to='team_images/', null=True, blank=True)
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    established_date = models.DateField()
    trophies_won = models.TextField(blank=True, null=True)
    team_summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Player(models.Model):
    player_image = models.ImageField(upload_to='player_images/', null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="players")
    player_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    nationality = models.CharField(max_length=100)
    awards = models.TextField(blank=True, null=True)
    career_summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Player"


class Format(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class PlayerStats(models.Model):
    player = models.ForeignKey(Player, related_name="stats", on_delete=models.CASCADE)
    format = models.ForeignKey(Format, on_delete=models.CASCADE)
    matches = models.IntegerField(default=0)
    runs = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    average = models.FloatField(default=0.0)
    strike_rate = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.player.name} - {self.format.name}"

    class Meta:
        unique_together = (("player", "format"),)


class ReportCard(models.Model):
    player = models.ForeignKey(Player, related_name="report_cards", on_delete=models.CASCADE)
    player_rank = models.IntegerField()
    date_of_report_card_generation = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = [('player', 'date_of_report_card_generation')]
