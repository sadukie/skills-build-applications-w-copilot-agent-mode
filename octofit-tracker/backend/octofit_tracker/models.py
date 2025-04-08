from djongo import models
from bson import ObjectId

class User(models.Model):
    _id = models.ObjectIdField(default=ObjectId, primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    user = models.EmbeddedField(model_container=User)

class Team(models.Model):
    _id = models.ObjectIdField(default=ObjectId, primary_key=True)
    name = models.CharField(max_length=255)
    members = models.JSONField(default=list)  # Initialize with an empty list by default

class Activity(models.Model):
    _id = models.ObjectIdField(default=ObjectId, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()

class Leaderboard(models.Model):
    _id = models.ObjectIdField(default=ObjectId, primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    _id = models.ObjectIdField(default=ObjectId, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()