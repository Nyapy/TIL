from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번째 {self.title} : {self.content}'