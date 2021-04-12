from django.db import models

# Create your models here.



class Team(models.Model):
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    designation = models.CharField(max_length=255, default='')
    photo = models.ImageField(upload_to= 'photo/%y/%m/%d/')
    facebook_link = models.URLField(max_length=255, default='')
    google_link = models.URLField(max_length=255, default='')
    twitter_link = models.URLField(max_length=255, default='')
    created_date= models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name
