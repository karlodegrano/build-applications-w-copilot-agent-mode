from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        tony = User.objects.create_user(username='ironman', email='tony@marvel.com', password='password', first_name='Tony', last_name='Stark', team=marvel)
        steve = User.objects.create_user(username='cap', email='steve@marvel.com', password='password', first_name='Steve', last_name='Rogers', team=marvel)
        bruce = User.objects.create_user(username='batman', email='bruce@dc.com', password='password', first_name='Bruce', last_name='Wayne', team=dc)
        clark = User.objects.create_user(username='superman', email='clark@dc.com', password='password', first_name='Clark', last_name='Kent', team=dc)

        # Create activities
        Activity.objects.create(user=tony, type='Run', duration=30, calories=300)
        Activity.objects.create(user=steve, type='Swim', duration=45, calories=400)
        Activity.objects.create(user=bruce, type='Cycle', duration=60, calories=500)
        Activity.objects.create(user=clark, type='Fly', duration=120, calories=1000)

        # Create workouts
        Workout.objects.create(name='Avengers HIIT', description='High intensity workout for Marvel heroes', team=marvel)
        Workout.objects.create(name='Justice League Strength', description='Strength training for DC heroes', team=dc)

        # Create leaderboard
        Leaderboard.objects.create(user=tony, score=1000)
        Leaderboard.objects.create(user=steve, score=900)
        Leaderboard.objects.create(user=bruce, score=950)
        Leaderboard.objects.create(user=clark, score=1100)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
