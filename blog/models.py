from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=300)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:250]

    def pub_date_formatted(self):
        return self.pub_date.strftime('%b. %e, %Y')
