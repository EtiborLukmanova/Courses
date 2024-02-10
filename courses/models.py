from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    duration = models.CharField(max_length=20)
    description = models.TextField()
    occurrence = models.IntegerField()
    time = models.IntegerField()

    def __str__(self):
        return self.course_name

