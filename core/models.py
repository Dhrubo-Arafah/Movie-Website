from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    picture = models.ImageField(upload_to='profile/')

    def __str__(self):
        return self.user


class File(models.Model):
    CHOICE = (
        ('movie', 'Movie'),
        ('music_video', 'Music Video'),
        ('music_audio', 'Music Audio'),
    )
    LANG = (
        ('bangla', 'Bangla'),
        ('hindi', 'Hindi'),
        ('english', 'English'),
        ('tamil', 'Tamil')
    )

    MOVIE_GENRE = (
        ('action', 'Action'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('comedy', 'Comedy'),
        ('sci-fi', 'Sci-Fi')
    )

    STATUS=(
        ('new_releases', 'New_Releases'),
        ('recently_added', 'Recently_Added'),
        ('trending', 'Trending'),
        ('must_watch', 'Must_Watch'),
    )

    logo = models.FileField(upload_to='file/logo')
    lang = models.CharField(max_length=250, choices=LANG, default=LANG[1][1])
    title = models.CharField(max_length=250)
    file = models.CharField(max_length=250)
    banner=models.FileField(upload_to='file/banner')
    trailer=models.CharField(max_length=250)
    thumbnail = models.FileField(upload_to='file/thumbnail')
    time=models.CharField(max_length=20)
    production=models.CharField(max_length=50)
    movie_genre = models.CharField(max_length=250, choices=MOVIE_GENRE, blank=True, default=MOVIE_GENRE[1][1])
    category = models.CharField(max_length=250, choices=CHOICE, default=CHOICE[1][1])
    release = models.CharField(max_length=100)
    starring=models.CharField(max_length=100)
    status = models.CharField(max_length=250, choices=STATUS, default=STATUS[1][1])
    description = models.CharField(max_length=5000)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
