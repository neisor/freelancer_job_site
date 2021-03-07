from django.db import models

class Job(models.Model):
    objects = models.Manager()
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
    email_for_job = models.EmailField()
    company = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    published_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.job_title + " | " + self.company + " | " + str(self.published_date)