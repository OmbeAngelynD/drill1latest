from django.db import models


class Post(models.Model):
        
    status_choices = (
        ('Draft', 'Draft'),
        ('Publish', 'Publish'),
    )

    title = models.CharField(max_length=250)
    abstract = models.TextField()
    body = models.TextField()
    publish = models.DateTimeField(null=False)
    created =models.DateTimeField(null=False)
    status = models.CharField(max_length=50, choices=status_choices)
               
    
    def __str__ (self):
        return self.title
