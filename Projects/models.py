from django.db import models

# Create your models here.
class Project(models.Model):
    psno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    technology = models.CharField(max_length=50)
    content = models.TextField(max_length=5000)
    slug = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="images", default="")
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title
    
     

