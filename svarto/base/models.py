from django.db import models
from django.utils.translation import gettext_lazy as _


class AboutUs(models.Model):
    image = models.ImageField(upload_to="about_us_images")
    text = models.TextField()


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to="team/")

    def __str__(self):
        return self.name


class WhatWeDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_code = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class NewsItem(models.Model):
    date = models.DateField()
    content = models.TextField()
    additional_text = models.TextField()

    def __str__(self):
        return f"News on {self.date} - {self.start_time} to {self.end_time}"
