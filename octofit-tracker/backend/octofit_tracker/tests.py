from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class BasicModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass', team=self.team)
        self.activity = Activity.objects.create(user=self.user, type='Run', duration=30, calories=300)
        self.workout = Workout.objects.create(name='Test Workout', description='Test Desc', team=self.team)
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)

    def test_user_team(self):
        self.assertEqual(self.user.team.name, 'Test Team')
    def test_activity(self):
        self.assertEqual(self.activity.type, 'Run')
    def test_workout(self):
        self.assertEqual(self.workout.team, self.team)
    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.score, 100)
