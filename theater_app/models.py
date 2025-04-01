from django.db import models
from theater_app.forms import User


class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.subject


class Movie(models.Model):
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=255, blank=True)
    homepage_image = models.CharField(max_length=255, blank=True)
    director = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    runtime = models.IntegerField(default=0)
    rating = models.CharField(max_length=10, blank=True)
    def __str__(self):
        return self.title

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='showtimes')
    time = models.TimeField()
    tickets_available = models.IntegerField(default=30)
    def __str__(self):
        return f"{self.movie.title} - {self.time}"


class Upcoming(models.Model):
    upcoming_movie = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    director = models.CharField(max_length=255, blank=True)
    image = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.upcoming_movie


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.showtime.movie.title} ({self.showtime.time}) - {self.quantity} Tickets"