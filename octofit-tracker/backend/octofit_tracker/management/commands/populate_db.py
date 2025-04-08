from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor', age=30),
            User(email='metalgeek@mhigh.edu', name='Tony Stark', age=35),
            User(email='zerocool@mhigh.edu', name='Steve Rogers', age=32),
            User(email='crashoverride@mhigh.edu', name='Natasha Romanoff', age=28),
            User(email='sleeptoken@mhigh.edu', name='Bruce Banner', age=40),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(name='Blue Team')
        team2 = Team(name='Gold Team')
        team1.members = [
            {"email": user.email, "name": user.name, "age": user.age} for user in users[:3]
        ]
        team2.members = [
            {"email": user.email, "name": user.name, "age": user.age} for user in users[3:]
        ]
        team1.save()
        team2.save()

        # Create activities
        # Convert timedelta to total seconds for the duration field
        activities = [
            Activity(user=users[0], activity_type='Cycling', duration=int(timedelta(hours=1).total_seconds())),
            Activity(user=users[1], activity_type='Crossfit', duration=int(timedelta(hours=2).total_seconds())),
            Activity(user=users[2], activity_type='Running', duration=int(timedelta(hours=1, minutes=30).total_seconds())),
            Activity(user=users[3], activity_type='Strength', duration=int(timedelta(minutes=30).total_seconds())),
            Activity(user=users[4], activity_type='Swimming', duration=int(timedelta(hours=1, minutes=15).total_seconds())),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=team1, score=100),
            Leaderboard(team=team2, score=90),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
